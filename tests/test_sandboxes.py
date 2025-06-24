import os
import sys
from datetime import datetime
from typing import cast

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import clusterfudge
from anthropic import (
    Anthropic,
    APIError,
    APIResponseValidationError,
    APIStatusError,
)
from anthropic.types.beta import (
    BetaMessage,
    BetaMessageParam,
    BetaTextBlock,
    BetaTextBlockParam,
    BetaToolResultBlockParam,
    BetaToolUnionParam,
    BetaToolUseBlock,
    BetaToolUseBlockParam,
)

SYSTEM_PROMPT = f"""<SYSTEM_CAPABILITY>
* You are utilising an Ubuntu virtual machine using x86_64 architecture with internet access.
* You can feel free to install Ubuntu applications with your bash tool. Use curl instead of wget.
* To open firefox, please just click on the firefox icon.  Note, firefox-esr is what is installed on your system.
* Using bash tool you can start GUI applications, but you need to set export DISPLAY=:1 and use a subshell. For example "(DISPLAY=:1 xterm &)". GUI apps run with bash tool will appear within your desktop environment, but they may take some time to appear. Take a screenshot to confirm it did.
* When using your bash tool with commands that are expected to output very large quantities of text, redirect into a tmp file and use str_replace_editor or `grep -n -B <lines before> -A <lines after> <query> <filename>` to confirm output.
* When viewing a page it can be helpful to zoom out so that you can see everything on the page.  Either that, or make sure you scroll down to see everything before deciding something isn't available.
* When using your computer function calls, they take a while to run and send back to you.  Where possible/feasible, try to chain multiple of these calls all into one function calls request.
* The current date is {datetime.today().strftime("%A, %B %-d, %Y")}.
</SYSTEM_CAPABILITY>

<ENVIRONMENT>
* There may be sidecar deployments running inside if your virtualized network that
will have records in your host files so you can reach, but they are not real sites/services.
* If you need to test connectivity to one of these services, start by opening Firefox, clicking on the address bar, and then entering 'http://$hostname:$port' into the address bar. Give this some time to load.
If firefox doesn't not resolve the page, try `nc -v $hostname $port`.
</ENVIRONMENT>

<IMPORTANT>
* When using Firefox, if a startup wizard appears, IGNORE IT.  Do not even click "skip this step".  Instead, click on the address bar where it says "Search or enter address", and enter the appropriate search term or URL there.

* If the item you are looking at is a pdf, if after taking a single screenshot of the pdf it seems that you want to read the entire document instead of trying to continue to read the pdf from your screenshots + navigation, determine the URL, use curl to download the pdf, install and use pdftotext to convert it to a text file, and then read that text file directly with your StrReplaceEditTool.
</IMPORTANT>"""

system = BetaTextBlockParam(
    type="text",
    text=f"{SYSTEM_PROMPT}",
)

tools: list[BetaToolUnionParam] = [
    {
        "type": "computer_20241022",
        "name": "computer",
        "display_width_px": 1024,
        "display_height_px": 768,
        "display_number": 1,
    },
    {"type": "text_editor_20241022", "name": "str_replace_editor"},
    {"type": "bash_20241022", "name": "bash"},
]


@pytest.mark.asyncio
async def test_sdk():
    """Test the full lifecycle of creating, using and deleting a Sandbox"""

    if "CLUSTERFUDGE_API_KEY" not in os.environ:
        pytest.skip()

    client = clusterfudge.Client(api_key=os.environ["CLUSTERFUDGE_API_KEY"])

    sandbox_id = await client.create_sandbox()
    assert sandbox_id, "Expected non-empty Sandbox ID"

    anthropic_client = Anthropic(
        api_key=os.environ["ANTHROPIC_API_KEY"],
    )

    initial_prompt = "Navigate to https://cnbc.com, click on the first article you see, save the text of the article to a file called joke.txt on the local machine, then, for fun, edit that file to prefix every proper noun with 'Mc', then dump the contents of that file into a terminal and finally, take a screenshot of the output."

    anthropic_messages = [
        BetaMessageParam(
            role="user", content=[BetaTextBlockParam(type="text", text=initial_prompt)]
        )
    ]

    num_calls = 0
    message_limit = 20
    while num_calls < message_limit:
        anthropic_messages = _maybe_filter_to_n_most_recent_images(anthropic_messages)

        try:
            response = anthropic_client.beta.messages.create(
                max_tokens=4096,
                messages=anthropic_messages,
                model="claude-3-5-sonnet-20241022",
                system=[system],
                tools=tools,
                betas=["computer-use-2024-10-22"],
            )
        except (APIStatusError, APIResponseValidationError) as e:
            raise Exception(f"APIStatusError: {e}")
        except APIError as e:
            raise Exception(f"APIError: {e}")

        num_calls += 1
        anthropic_messages.append(
            BetaMessageParam(
                role="assistant",
                content=_message_to_params(response),
            )
        )

        try:
            anthropic_messages = await client.claude_computer_use(
                sandbox_id, anthropic_messages
            )
        except Exception as e:
            await client.delete_sandbox(sandbox_id)
            pytest.fail(
                f"failed to perform computer-use action inside Sandbox: {str(e)}"
            )

    try:
        await client.delete_sandbox(sandbox_id)
    except Exception as e:
        pytest.fail(f"Failed to delete Sandbox: {str(e)}")


def _message_to_params(
    message: BetaMessage,
) -> list[BetaTextBlockParam | BetaToolUseBlockParam]:
    res: list[BetaTextBlockParam | BetaToolUseBlockParam] = []
    if not message.content:
        return res

    for block in message.content:
        if isinstance(block, BetaTextBlock):
            res.append(BetaTextBlockParam(type="text", text=block.text))
        elif isinstance(block, BetaToolUseBlock):
            res.append(
                BetaToolUseBlockParam(
                    type="tool_use", id=block.id, input=block.input, name=block.name
                )
            )
    return res


def _maybe_filter_to_n_most_recent_images(
    messages: list[BetaMessageParam], max_images: int = 3
) -> list[BetaMessageParam]:
    tool_result_blocks = cast(
        list[BetaToolResultBlockParam],
        [
            item
            for message in reversed(messages)  # Reverse to process most recent first
            for item in (
                message["content"] if isinstance(message["content"], list) else []
            )
            if isinstance(item, dict) and item.get("type") == "tool_result"
        ],
    )

    image_count = 0
    for tool_result in tool_result_blocks:
        if isinstance(tool_result.get("content"), list):
            new_content = []
            for content in tool_result.get("content", []):
                if isinstance(content, dict) and content.get("type") == "image":
                    if image_count < max_images:
                        new_content.append(content)
                        image_count += 1
                else:
                    new_content.append(content)
            tool_result["content"] = new_content

    return messages
