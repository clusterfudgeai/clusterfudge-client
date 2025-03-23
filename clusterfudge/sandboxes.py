import base64
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


async def _do_with_anthropic_shim(
    clusterfudge_client: Client, sandbox_id: str, name: ToolName, d: dict
) -> Union[BetaTextBlockParam, BetaImageBlockParam]:
    response = await clusterfudge_client.claude_computer_use(
        sandbox_id,
        [
            BetaMessageParam(
                role="assistant",
                content=[
                    BetaToolUseBlockParam(
                        type="tool_use",
                        name=name,
                        id=str(uuid.uuid4()),
                        input=d,
                    ),
                ],
            )
        ],
    )

    try:
        first_message: BetaMessageParam = response[-1]
        first_tool_use: BetaToolResultBlockParam = first_message["content"][0]  # type: ignore
        first_tool_use_content = first_tool_use["content"][0]  # type: ignore

        return first_tool_use_content  # type: ignore
    except Exception as e:
        raise RuntimeError(f"Error calling sandbox for tool {name}: {e}") from e


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

        # Text contains a JSON object with x and y keys.
        as_dict = json.loads(_text_result_or_raise(tool_result))

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

    def run(self, command: str) -> dict:
        """Run a command in the sandbox.

        Args:
            command: The bash command to run

        Returns:
            A dictionary containing stdout, stderr, error info, and whether the
            command is still running
        """
        raise NotImplementedError()

    def restart(self) -> None:
        """Restart the bash session, killing any running processes."""
        raise NotImplementedError()


class FileEditorClient:
    """Client for file operations in the sandbox."""

    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        self.sandbox_id = sandbox_id
        self.clusterfudge_client = clusterfudge_client

    def view(self, path: str, view_range: list[int] | None = None) -> str:
        """View file contents.

        Args:
            path: Path to the file
            view_range: Optional range of lines to view

        Returns:
            File contents
        """
        raise NotImplementedError()

    def str_replace(self, path: str, old_str: str, new_str: str) -> str:
        """Replace a string in a file.

        Args:
            path: Path to the file
            old_str: String to replace
            new_str: Replacement string

        Returns:
            Result message
        """
        raise NotImplementedError()

    def insert(self, path: str, insert_line: int, new_str: str) -> str:
        """Insert a string at a specific line in a file.

        Args:
            path: Path to the file
            insert_line: Line number to insert at
            new_str: String to insert

        Returns:
            Result message
        """
        raise NotImplementedError()

    def undo_edit(self, path: str) -> str:
        """Undo the last edit to a file.

        Args:
            path: Path to the file

        Returns:
            Result message
        """
        raise NotImplementedError()

    def create(self, path: str, file_text: str) -> str:
        """Create a new file.

        Args:
            path: Path to create the file at
            file_text: Content for the file

        Returns:
            Result message
        """
        raise NotImplementedError()


class SandboxClient:
    def __init__(self, sandbox_id: str, clusterfudge_client: Client):
        self.sandbox_id = sandbox_id
        self._computer = ComputerClient(self.sandbox_id, clusterfudge_client)
        self._basher = BasherClient(self.sandbox_id, clusterfudge_client)
        self._file_editor = FileEditorClient(self.sandbox_id, clusterfudge_client)

    def get_sandbox(self):
        pass

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
