import base64
import dataclasses
import json
import uuid
from typing import Any, Literal, Union

from anthropic.types.beta import (
    BetaImageBlockParam,
    BetaMessageParam,
    BetaTextBlockParam,
    BetaToolResultBlockParam,
    BetaToolUseBlockParam,
)
from clusterfudge_proto.sandboxespb import sandboxes_pb2

from .clusterfudge import Client

TOOL_NAME_COMPUTER = "computer"
TOOL_NAME_BASH = "bash"
TOOL_NAME_STR_REPLACE_EDITOR = "str_replace_editor"

# Computer Use Actions (`action` param of tool_use input)
ACTION_KEY = "key"
ACTION_TYPE = "type"
ACTION_MOUSE_MOVE = "mouse_move"
ACTION_LEFT_CLICK = "left_click"
ACTION_LEFT_CLICK_DRAG = "left_click_drag"
ACTION_RIGHT_CLICK = "right_click"
ACTION_MIDDLE_CLICK = "middle_click"
ACTION_DOUBLE_CLICK = "double_click"
ACTION_TRIPLE_CLICK = "triple_click"
ACTION_SCREENSHOT = "screenshot"
ACTION_CURSOR_POSITION = "cursor_position"
ACTION_LEFT_MOUSE_DOWN = "left_mouse_down"
ACTION_LEFT_MOUSE_UP = "left_mouse_up"
ACTION_SCROLL = "scroll"
ACTION_HOLD_KEY = "hold_key"
ACTION_WAIT = "wait"


# Scroll directions
SCROLL_UP = "up"
SCROLL_DOWN = "down"
SCROLL_LEFT = "left"
SCROLL_RIGHT = "right"

SCROLL_DIRECTIONS = (SCROLL_UP, SCROLL_DOWN, SCROLL_LEFT, SCROLL_RIGHT)

ToolName = Literal["computer", "bash", "str_replace_editor"]

ACTIONSET_CLICKS = (
    ACTION_LEFT_CLICK,
    ACTION_RIGHT_CLICK,
    ACTION_MIDDLE_CLICK,
    ACTION_DOUBLE_CLICK,
    ACTION_TRIPLE_CLICK,
)

COMPUTER_TOOL_INPUT_SCHEMA = {
    "properties": {
        "action": {
            "description": "The action to perform. The available actions are:\n"
            "* `key`: Press a key or key-combination on the keyboard.\n"
            "  - This supports xdotool's `key` syntax.\n"
            '  - Examples: "a", "Return", "alt+Tab", "ctrl+s", "Up", "KP_0" (for the numpad 0 key).\n'
            "* `hold_key`: Hold down a key or multiple keys for a specified duration (in seconds). Supports the same syntax as `key`.\n"
            "* `type`: Type a string of text on the keyboard.\n"
            "* `cursor_position`: Get the current (x, y) pixel coordinate of the cursor on the screen.\n"
            "* `mouse_move`: Move the cursor to a specified (x, y) pixel coordinate on the screen.\n"
            "* `left_mouse_down`: Press the left mouse button.\n"
            "* `left_mouse_up`: Release the left mouse button.\n"
            "* `left_click`: Click the left mouse button at the specified (x, y) pixel coordinate on the screen. You can also include a key combination to hold down while clicking using the `text` parameter.\n"
            "* `left_click_drag`: Click and drag the cursor from `start_coordinate` to a specified (x, y) pixel coordinate on the screen.\n"
            "* `right_click`: Click the right mouse button at the specified (x, y) pixel coordinate on the screen.\n"
            "* `middle_click`: Click the middle mouse button at the specified (x, y) pixel coordinate on the screen.\n"
            "* `double_click`: Double-click the left mouse button at the specified (x, y) pixel coordinate on the screen.\n"
            "* `triple_click`: Triple-click the left mouse button at the specified (x, y) pixel coordinate on the screen.\n"
            "* `scroll`: Scroll the screen in a specified direction by a specified amount of clicks of the scroll wheel, at the specified (x, y) pixel coordinate. DO NOT use PageUp/PageDown to scroll.\n"
            "* `wait`: Wait for a specified duration (in seconds).\n"
            "* `screenshot`: Take a screenshot of the screen.",
            "enum": [
                "key",
                "hold_key",
                "type",
                "cursor_position",
                "mouse_move",
                "left_mouse_down",
                "left_mouse_up",
                "left_click",
                "left_click_drag",
                "right_click",
                "middle_click",
                "double_click",
                "triple_click",
                "scroll",
                "wait",
                "screenshot",
            ],
            "type": "string",
        },
        "coordinate": {
            "description": "(x, y): The x (pixels from the left edge) and y (pixels from the top edge) coordinates to move the mouse to. Required only by `action=mouse_move` and `action=left_click_drag`.",
            "type": "array",
        },
        "duration": {
            "description": "The duration to hold the key down for. Required only by `action=hold_key` and `action=wait`.",
            "type": "integer",
        },
        "scroll_amount": {
            "description": "The number of 'clicks' to scroll. Required only by `action=scroll`.",
            "type": "integer",
        },
        "scroll_direction": {
            "description": "The direction to scroll the screen. Required only by `action=scroll`.",
            "enum": ["up", "down", "left", "right"],
            "type": "string",
        },
        "start_coordinate": {
            "description": "(x, y): The x (pixels from the left edge) and y (pixels from the top edge) coordinates to start the drag from. Required only by `action=left_click_drag`.",
            "type": "array",
        },
        "text": {
            "description": "Required only by `action=type`, `action=key`, and `action=hold_key`. Can also be used by click or scroll actions to hold down keys while clicking or scrolling.",
            "type": "string",
        },
    },
    "required": ["action"],
    "type": "object",
}

TEXT_EDITOR_INPUT_SCHEMA = {
    "properties": {
        "command": {
            "description": "The commands to run. Allowed options are: `view`, `create`, `str_replace`, `insert`, `undo_edit`.",
            "enum": ["view", "create", "str_replace", "insert", "undo_edit"],
            "type": "string",
        },
        "file_text": {
            "description": "Required parameter of `create` command, with the content of the file to be created.",
            "type": "string",
        },
        "insert_line": {
            "description": "Required parameter of `insert` command. The `new_str` will be inserted AFTER the line `insert_line` of `path`.",
            "type": "integer",
        },
        "new_str": {
            "description": "Optional parameter of `str_replace` command containing the new string (if not given, no string will be added). Required parameter of `insert` command containing the string to insert.",
            "type": "string",
        },
        "old_str": {
            "description": "Required parameter of `str_replace` command containing the string in `path` to replace.",
            "type": "string",
        },
        "path": {
            "description": "Absolute path to file or directory, e.g. `/repo/file.py` or `/repo`.",
            "type": "string",
        },
        "view_range": {
            "description": "Optional parameter of `view` command when `path` points to a file. If none is given, the full file is shown. If provided, the file will be shown in the indicated line number range, e.g. [11, 12] will show lines 11 and 12. Indexing at 1 to start. Setting `[start_line, -1]` shows all lines from `start_line` to the end of the file.",
            "items": {"type": "integer"},
            "type": "array",
        },
    },
    "required": ["command", "path"],
    "type": "object",
}

BASH_INPUT_SCHEMA = {
    "properties": {
        "command": {
            "description": "The bash command to run. Required unless the tool is being restarted.",
            "type": "string",
        },
        "restart": {
            "description": "Specifying true will restart this tool. Otherwise, leave this unspecified.",
            "type": "boolean",
        },
    }
}


@dataclasses.dataclass
class SandboxAuthToken:
    token: str


async def _do_with_anthropic_shim(
    clusterfudge_client: Client, sandbox_id: str, name: ToolName, d: dict
) -> Union[BetaTextBlockParam, BetaImageBlockParam]:
    tool_use_id = str(uuid.uuid4())

    response = await clusterfudge_client.claude_computer_use(
        sandbox_id,
        [
            BetaMessageParam(
                role="assistant",
                content=[
                    BetaToolUseBlockParam(
                        type="tool_use",
                        name=name,
                        id=tool_use_id,
                        input=d,
                    ),
                ],
            )
        ],
    )

    empty_response = BetaTextBlockParam(
        type="text",
        text="",
    )

    try:
        first_message: BetaMessageParam = response[-1]

        first_tool_use: BetaToolResultBlockParam = first_message["content"][0]  # type: ignore

        if "is_error" in first_tool_use and first_tool_use["is_error"]:
            error_message = "unknown error"

            if "content" not in first_tool_use:
                raise RuntimeError(
                    f"Tool {name} ({tool_use_id}) returned an error with no content"
                )

            error_message = first_tool_use["content"][0]["text"]  # type: ignore

            raise RuntimeError(
                f"Tool {name} ({tool_use_id}) returned an error: {error_message}"
            )

        first_tool_use_content = first_tool_use["content"][0]  # type: ignore

        return first_tool_use_content  # type: ignore
    except KeyError:
        return empty_response
    except IndexError:
        return empty_response
    except Exception as e:
        raise RuntimeError(f"Error calling sandbox for tool {name}: {e}") from e


def _get_error(r: BetaToolResultBlockParam) -> str:
    # Error responses look like this:
    #     {
    #   "content": [
    #     {
    #       "text": "failed to get cursor position: \"X\" coordinate prefix not found in: x:921 y:691 screen:0 window:6291469",
    #       "type": "text"
    #     }
    #   ],
    #   "is_error": true,
    #   "tool_use_id": "c92d350a-0d18-4dd1-a2e3-d4b77a20c999",
    #   "type": "tool_result"
    # }
    if "content" not in r:
        return "unknown error"

    if isinstance(r["content"], str):
        return r["content"]

    if not isinstance(r["content"], list):
        return "unknown error"

    if len(r["content"]) == 0:
        return "unknown error"

    if not isinstance(r["content"][0], dict):
        return "unknown error"

    if "text" not in r["content"][0]:
        return "unknown error"

    return r["content"][0]["text"]


def _text_result_or_raise(
    tool_result: Union[BetaTextBlockParam, BetaImageBlockParam],
) -> str:
    if not ("type" in tool_result and tool_result["type"] == "text"):
        raise RuntimeError("Key returned non-text data")

    return tool_result["text"]  # type: ignore


def _img_result_or_raise(
    tool_result: Union[BetaTextBlockParam, BetaImageBlockParam],
) -> bytes:
    if not ("type" in tool_result and tool_result["type"] == "image"):
        raise RuntimeError("Screenshot returned non-image data")

    return base64.b64decode(tool_result["source"]["data"])  # type: ignore


class ComputerClient:
    """Client for interacting with the sandbox's computer interface."""

    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        self.sandbox_id = sandbox_id
        self.clusterfudge_client = clusterfudge_client

    async def _do_action(
        self, d: dict
    ) -> Union[BetaTextBlockParam, BetaImageBlockParam]:
        return await _do_with_anthropic_shim(
            self.clusterfudge_client,
            self.sandbox_id,
            TOOL_NAME_COMPUTER,
            d,
        )

    async def screenshot(self) -> bytes:
        tool_result = await self._do_action(
            {
                "action": ACTION_SCREENSHOT,
            }
        )

        return _img_result_or_raise(tool_result)

    async def key(self, text: str) -> str:
        tool_result = await self._do_action(
            {
                "action": ACTION_KEY,
                "text": text,
            },
        )

        return _text_result_or_raise(tool_result)

    async def type(self, text: str) -> str:
        tool_result = await self._do_action(
            {
                "action": ACTION_TYPE,
                "text": text,
            },
        )

        return _text_result_or_raise(tool_result)

    async def mouse_move(self, x: int, y: int) -> None:
        await self._do_action(
            {
                "action": ACTION_MOUSE_MOVE,
                "coordinate": [x, y],
            },
        )

    async def left_click_drag(self, x: int, y: int) -> None:
        await self._do_action(
            {
                "action": ACTION_LEFT_CLICK_DRAG,
                "coordinate": [x, y],
            },
        )

    async def cursor_position(self) -> tuple[int, int]:
        """Get the current cursor position.

        Returns:
            Tuple of (x, y) coordinates
        """

        tool_result = await self._do_action(
            {
                "action": ACTION_CURSOR_POSITION,
            },
        )

        text_result = _text_result_or_raise(tool_result)

        # Text contains a JSON object with x and y keys.
        try:
            as_dict = json.loads(text_result)
        except json.JSONDecodeError as e:
            raise RuntimeError(
                f"Cursor position returned non-JSON data: {e} (text: {text_result})"
            ) from e

        return as_dict["x"], as_dict["y"]

    async def click(
        self,
        action: str,
        x: int | None = None,
        y: int | None = None,
        key: str | None = None,
    ) -> None:
        """Perform a click action.

        Args:
            action: The type of click action
            x: Optional X coordinate
            y: Optional Y coordinate
            key: Optional key to hold during click
        """

        if action not in ACTIONSET_CLICKS:
            raise ValueError(
                f"Invalid action '{action}', must be one of {ACTIONSET_CLICKS}"
            )

        if x is not None and y is None:
            raise ValueError("x coordinate is provided but y coordinate is not.")

        if y is not None and x is None:
            raise ValueError("y coordinate is provided but x coordinate is not.")

        args: dict[str, Any] = {"action": action}
        if x is not None:
            args["coordinate"] = [x, y]
        if key is not None:
            args["key"] = key

        await self._do_action(args)

    async def left_mouse_down(self) -> None:
        """Press the left mouse button down."""
        await self._do_action(
            {
                "action": ACTION_LEFT_MOUSE_DOWN,
            },
        )

    async def left_mouse_up(self) -> None:
        """Release the left mouse button."""
        await self._do_action(
            {
                "action": ACTION_LEFT_MOUSE_UP,
            },
        )

    async def scroll(
        self,
        direction: str,
        amount: int,
        x: int | None = None,
        y: int | None = None,
        key: str | None = None,
    ) -> None:
        """Scroll in a direction.

        Args:
            direction: Scroll direction ("up", "down", "left", "right")
            amount: Amount to scroll
            x: Optional X coordinate to scroll at
            y: Optional Y coordinate to scroll at
            key: Optional key to hold during scroll
        """

        if direction not in SCROLL_DIRECTIONS:
            raise ValueError(
                f"Invalid direction '{direction}', must be one of {SCROLL_DIRECTIONS}"
            )

        if x is not None and y is None:
            raise ValueError("x coordinate is provided but y coordinate is not.")

        if y is not None and x is None:
            raise ValueError("y coordinate is provided but x coordinate is not.")

        args: dict[str, Any] = {
            "action": ACTION_SCROLL,
            "scroll_direction": direction,
            "scroll_amount": amount,
        }
        if x is not None:
            args["coordinate"] = [x, y]
        if key is not None:
            args["key"] = key

        await self._do_action(args)

    async def hold_key(self, text: str, duration: float) -> None:
        """Hold a key for a duration.

        Args:
            text: The key to hold
            duration: Duration in seconds
        """
        await self._do_action(
            {
                "action": ACTION_HOLD_KEY,
                "text": text,
                "duration": duration,
            },
        )

    async def wait(self, duration: float) -> bytes:
        """Wait for a duration and return a screenshot.

        Args:
            duration: Time to wait in seconds

        Returns:
            Screenshot image data
        """
        tool_result = await self._do_action(
            {
                "action": ACTION_WAIT,
                "duration": duration,
            },
        )

        return _img_result_or_raise(tool_result)


class BasherClient:
    """Client for running bash commands in the sandbox."""

    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        self.sandbox_id = sandbox_id
        self.clusterfudge_client = clusterfudge_client

    async def _do_action(
        self, d: dict
    ) -> Union[BetaTextBlockParam, BetaImageBlockParam]:
        return await _do_with_anthropic_shim(
            self.clusterfudge_client,
            self.sandbox_id,
            TOOL_NAME_BASH,
            d,
        )

    async def run(self, command: str) -> dict:
        """Run a command in the sandbox.

        Args:
            command: The bash command to run

        Returns:
            A dictionary containing stdout, stderr, error info, and whether the
            command is still running
        """
        tool_result = await self._do_action({"command": command})

        output = _text_result_or_raise(tool_result)

        # Parse the result to determine success/failure
        is_error = tool_result.get("is_error", False)

        if is_error:
            # Try to extract stderr and stdout from error message
            parts = output.split("\n", 1)
            stderr = parts[0] if len(parts) > 0 else output
            stdout = parts[1] if len(parts) > 1 else ""

            return {
                "stdout": stdout,
                "stderr": stderr,
                "error": stderr,
                "still_running": False,
            }
        else:
            return {
                "stdout": output,
                "stderr": "",
                "error": None,
                "still_running": "still running" in output.lower(),
            }

    async def restart(self) -> None:
        """Restart the bash session, killing any running processes."""
        await self._do_action({"restart": True})


class FileEditorClient:
    """Client for file operations in the sandbox."""

    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        self.sandbox_id = sandbox_id
        self.clusterfudge_client = clusterfudge_client

    async def _do_action(
        self, d: dict
    ) -> Union[BetaTextBlockParam, BetaImageBlockParam]:
        return await _do_with_anthropic_shim(
            self.clusterfudge_client,
            self.sandbox_id,
            TOOL_NAME_STR_REPLACE_EDITOR,
            d,
        )

    async def view(self, path: str, view_range: list[int] | None = None) -> str:
        """View file contents.

        Args:
            path: Path to the file
            view_range: Optional range of lines to view

        Returns:
            File contents
        """
        params: dict[str, Any] = {
            "command": "view",
            "path": path,
        }

        if view_range:
            params["view_range"] = view_range

        tool_result = await self._do_action(params)
        return _text_result_or_raise(tool_result)

    async def str_replace(self, path: str, old_str: str, new_str: str) -> str:
        """Replace a string in a file.

        Args:
            path: Path to the file
            old_str: String to replace
            new_str: Replacement string

        Returns:
            Result message
        """
        tool_result = await self._do_action(
            {
                "command": "str_replace",
                "path": path,
                "old_str": old_str,
                "new_str": new_str,
            }
        )

        return _text_result_or_raise(tool_result)

    async def insert(self, path: str, insert_line: int, new_str: str) -> str:
        """Insert a string at a specific line in a file.

        Args:
            path: Path to the file
            insert_line: Line number to insert at
            new_str: String to insert

        Returns:
            Result message
        """
        tool_result = await self._do_action(
            {
                "command": "insert",
                "path": path,
                "insert_line": insert_line,
                "new_str": new_str,
            }
        )

        return _text_result_or_raise(tool_result)

    async def undo_edit(self, path: str) -> str:
        """Undo the last edit to a file.

        Args:
            path: Path to the file

        Returns:
            Result message
        """
        tool_result = await self._do_action({"command": "undo_edit", "path": path})

        return _text_result_or_raise(tool_result)

    async def create(self, path: str, file_text: str) -> str:
        """Create a new file.

        Args:
            path: Path to create the file at
            file_text: Content for the file

        Returns:
            Result message
        """
        tool_result = await self._do_action(
            {"command": "create", "path": path, "file_text": file_text}
        )

        return _text_result_or_raise(tool_result)


class TerminalClient:
    """Client for interacting with the sandbox's terminal interface."""

    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        self.sandbox_id = sandbox_id
        self.clusterfudge_client = clusterfudge_client

    async def write_to_terminal(
        self, terminal_id: str, input_text: str, wait_for_response_ms: int = 500
    ) -> dict:
        """Write text to a terminal and wait for a response.

        Args:
            terminal_id: The ID of the terminal to write to
            input_text: The text to write to the terminal
            wait_for_response_ms: Time to wait for a response in milliseconds

        Returns:
            A dictionary containing stdout, stderr, and any error information
        """
        response = await self.clusterfudge_client.write_to_terminal(
            self.sandbox_id, terminal_id, input_text, wait_for_response_ms
        )

        return {
            "stdout": response.get("stdout", ""),
            "stderr": response.get("stderr", ""),
            "error": response.get("exec_error", None),
        }

    async def kill_terminal(self, terminal_id: str) -> dict:
        """Kill a terminal.

        Args:
            terminal_id: The ID of the terminal to kill

        Returns:
            A dictionary containing success status and any error information
        """
        response = await self.clusterfudge_client.kill_terminal(
            self.sandbox_id, terminal_id
        )

        return {
            "success": response.get("success", False),
            "error": response.get("error", None),
        }

    async def reset_terminal(self, terminal_id: str) -> dict:
        """Reset a terminal.

        Args:
            terminal_id: The ID of the terminal to reset

        Returns:
            A dictionary containing success status and any error information
        """
        response = await self.clusterfudge_client.reset_terminal(
            self.sandbox_id, terminal_id
        )

        return {
            "success": response.get("success", False),
            "error": response.get("error", None),
        }

    async def reset_all_terminals(self) -> dict:
        """Reset all terminals in the sandbox.

        Returns:
            A dictionary containing success status and any error information
        """
        response = await self.clusterfudge_client.reset_all_terminals(self.sandbox_id)

        return {
            "success": response.get("success", False),
            "error": response.get("error", None),
        }

    async def get_terminal_history(self, terminal_id: str) -> dict:
        """Get command history from a terminal.

        Args:
            terminal_id: The ID of the terminal to get history from

        Returns:
            A dictionary containing command history and any error information
        """
        response = await self.clusterfudge_client.get_terminal_history(
            self.sandbox_id, terminal_id
        )

        return {
            "commands": response.get("commands", []),
            "error": response.get("error", None),
        }


@dataclasses.dataclass
class ProcessResponse:
    stdin: list[str]
    stdout: str
    stderr: str
    terminal_output: str
    process_error: str | None
    exit_code: int | None


class ProcessClient:
    """Client for interacting with processes in the sandbox."""

    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        self.sandbox_id = sandbox_id
        self.clusterfudge_client = clusterfudge_client

    async def write_to_process(
        self, process_id: str, input_bytes: bytes | str, wait_for_response_ms: int = 300
    ) -> ProcessResponse:
        """Write bytes to a process and wait for a response.

        Args:
            process_id: The ID of the process to write to
            input_bytes: The bytes to write to the process stdin
            wait_for_response_ms: Time to wait for a response in milliseconds

        Returns:
            A dictionary containing stdin, stdout, stderr, terminal output,
            process error, exit code, and sandbox error information.
        """
        response = await self.clusterfudge_client.write_to_process(
            self.sandbox_id, process_id, input_bytes, wait_for_response_ms
        )

        return ProcessResponse(
            stdin=response["stdin"],
            stdout=response["stdout"],
            stderr=response["stderr"],
            terminal_output=response["terminal_output"],
            process_error=response["process_error"],
            exit_code=response["exit_code"],
        )

    async def kill_process(self, process_id: str) -> dict:
        """Kill a process.

        Args:
            process_id: The ID of the process to kill

        Returns:
            A dictionary containing success status and any error information.
        """
        response = await self.clusterfudge_client.kill_process(
            self.sandbox_id, process_id
        )
        return response

    async def get_process(self, process_id: str) -> dict:
        """Get information about a process.

        Args:
            process_id: The ID of the process to get info for

        Returns:
            A dictionary containing stdin, stdout, stderr, terminal output,
            process error, exit code, and sandbox error information.
        """
        response = await self.clusterfudge_client.get_process(
            self.sandbox_id, process_id
        )
        return response


class FileManagerClient:
    """Client for managing files in the sandbox."""

    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        self.sandbox_id = sandbox_id
        self.clusterfudge_client = clusterfudge_client

    async def download_file(self, absolute_file_path: str) -> tuple[bytes, str | None]:
        """Download a file from the sandbox.

        Args:
            absolute_file_path: The absolute path to the file in the sandbox

        Returns:
            A tuple of (file contents as bytes, error message if any)
        """
        response = await self.clusterfudge_client.download_file(
            self.sandbox_id, absolute_file_path
        )

        return response.get("contents", b""), response.get("sandbox_error")

    async def download_folder(
        self, absolute_folder_path: str
    ) -> tuple[bytes, str | None]:
        """Download a folder from the sandbox as a zip file.

        Args:
            absolute_folder_path: The absolute path to the folder in the sandbox

        Returns:
            A tuple of (zipped folder contents as bytes, error message if any)
        """
        response = await self.clusterfudge_client.download_folder(
            self.sandbox_id, absolute_folder_path
        )

        return response.get("zipped_contents", b""), response.get("sandbox_error")

    async def create_file(
        self, absolute_file_path: str, contents: bytes, overwrite_existing: bool = False
    ) -> dict:
        """Create a file in the sandbox.

        Args:
            absolute_file_path: The absolute path of the file to create.
            contents: The binary contents of the file.
            overwrite_existing: Whether to overwrite the file if it already exists.

        Returns:
            A dictionary containing the response with sandbox_error field if there was an error.
        """
        response = await self.clusterfudge_client.create_file(
            sandbox_id=self.sandbox_id,
            absolute_file_path=absolute_file_path,
            contents=contents,
            overwrite_existing=overwrite_existing,
        )
        return response


class AuditLog:
    """Audit log entry for a sandbox containing a request and response."""

    def __init__(self, log: sandboxes_pb2.ComputerUseRequestLog):
        self.raw_log = log

    def request(self) -> dict:
        return json.loads(self.raw_log.raw_request_contents)

    def response(self) -> dict:
        return json.loads(self.raw_log.raw_response_contents)

    def get_response_images(self) -> list[bytes]:
        """Extract screenshot data from the response if present.

        Returns:
            The decoded screenshot data as bytes, or None if no screenshot found
        """
        screenshots = []
        response_data = self.response()
        for item in response_data.get("content", []):
            if (
                item.get("type") == "image"
                and item.get("source", {}).get("media_type") == "image/png"
            ):
                base64_data = item["source"]["data"]
                screenshots.append(base64.b64decode(base64_data))
        return screenshots


class SandboxClient:
    """Main client for interacting with a Clusterfudge Sandbox.

    This client provides access to various tools for interacting with the sandbox:
    - Computer: UI interactions like screenshots, mouse, keyboard
    - Basher: Command execution
    - FileEditor: File operations
    - Terminal: Direct terminal interaction
    - FileManager: File download operations
    - Process: Process interaction (write, kill, get)
    """

    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        """Initialize a SandboxClient.

        Args:
            sandbox_id: The ID of the sandbox to interact with
            clusterfudge_client: An initialized Clusterfudge Client
        """
        self.sandbox_id = sandbox_id
        self.clusterfudge_client = clusterfudge_client
        self._computer = ComputerClient(self.sandbox_id, clusterfudge_client)
        self._basher = BasherClient(self.sandbox_id, clusterfudge_client)
        self._file_editor = FileEditorClient(self.sandbox_id, clusterfudge_client)
        self._terminal = TerminalClient(self.sandbox_id, clusterfudge_client)
        self._file_manager = FileManagerClient(self.sandbox_id, clusterfudge_client)
        self._process = ProcessClient(self.sandbox_id, clusterfudge_client)

    def computer(self) -> ComputerClient:
        """Get the computer interface client.

        Returns:
            ComputerClient instance
        """
        return self._computer

    def basher(self) -> BasherClient:
        """Get the bash command client.

        Returns:
            BasherClient instance
        """
        return self._basher

    def file_editor(self) -> FileEditorClient:
        """Get the file editor client.

        Returns:
            FileEditorClient instance
        """
        return self._file_editor

    def terminal(self) -> TerminalClient:
        """Get the terminal client.

        Returns:
            TerminalClient instance
        """
        return self._terminal

    def file_manager(self) -> FileManagerClient:
        """Get the file manager client.

        Returns:
            FileManagerClient instance
        """
        return self._file_manager

    def process(self) -> ProcessClient:
        """Get the process client.

        Returns:
            ProcessClient instance
        """
        return self._process

    async def mint_auth_token(self) -> SandboxAuthToken:
        """Mint an auth token for the sandbox.

        Returns:
            An auth token for the sandbox.
        """
        response = await self.clusterfudge_client.sandbox_stub.MintAuthToken(
            sandboxes_pb2.MintAuthTokenRequest(machine_id=self.sandbox_id)
        )
        return SandboxAuthToken(token=response.auth_token)

    async def get_audit_logs(self) -> list[AuditLog]:
        """Get audit logs for the sandbox.

        Returns:
            A list of audit logs.
        """
        response = await self.clusterfudge_client.beta.get_sandbox_audit_logs(
            sandboxes_pb2.GetComputerUseRequestLogsRequest(
                machine_id=self.sandbox_id,
            )
        )
        return list(AuditLog(log) for log in response.logs)
