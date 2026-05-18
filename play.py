"""GitHub Issues-powered Tic-Tac-Toe engine for the profile README."""

from __future__ import annotations

import json
import os
import sys
from functools import lru_cache
from pathlib import Path
from urllib.parse import urlencode

STATE_PATH = Path("matrix.json")
README_PATH = Path("README.md")
USERNAME = "Aaditya-Golash"
START_TAG = "<!-- TTT:START -->"
END_TAG = "<!-- TTT:END -->"
EMPTY = " "
HUMAN = "X"
COMPUTER = "O"
WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def fresh_state() -> dict[str, object]:
    """Return a new empty game state."""
    return {"board": [EMPTY] * 9, "turn": HUMAN, "status": "ONGOING"}


def load_state() -> dict[str, object]:
    """Load the current board, falling back to a fresh game if needed."""
    if not STATE_PATH.exists():
        return fresh_state()

    with STATE_PATH.open("r", encoding="utf-8") as state_file:
        state = json.load(state_file)

    board = state.get("board")
    if not isinstance(board, list) or len(board) != 9:
        return fresh_state()

    if state.get("status") != "ONGOING":
        return fresh_state()

    return state


def save_state(state: dict[str, object]) -> None:
    """Persist the board state to disk."""
    with STATE_PATH.open("w", encoding="utf-8") as state_file:
        json.dump(state, state_file, indent=2)
        state_file.write("\n")


def check_result(board: list[str]) -> str | None:
    """Return X, O, DRAW, or None for an unfinished board."""
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    if EMPTY not in board:
        return "DRAW"
    return None


def parse_move(issue_title: str) -> int | None:
    """Parse an issue title in the format play:<cell>, where cell is 0-8."""
    prefix = "play:"
    if not issue_title.startswith(prefix):
        return None

    try:
        move = int(issue_title.removeprefix(prefix).strip())
    except ValueError:
        return None

    if 0 <= move <= 8:
        return move
    return None


@lru_cache(maxsize=None)
def minimax(board_key: tuple[str, ...], is_computer_turn: bool) -> int:
    """Score board states so O plays optimally and X cannot force a win."""
    board = list(board_key)
    result = check_result(board)
    if result == COMPUTER:
        return 1
    if result == HUMAN:
        return -1
    if result == "DRAW":
        return 0

    scores = []
    marker = COMPUTER if is_computer_turn else HUMAN
    for index, value in enumerate(board):
        if value == EMPTY:
            board[index] = marker
            scores.append(minimax(tuple(board), not is_computer_turn))
            board[index] = EMPTY

    return max(scores) if is_computer_turn else min(scores)


def choose_computer_move(board: list[str]) -> int | None:
    """Pick the strongest available O move using minimax."""
    best_score = -2
    best_move = None

    for index, value in enumerate(board):
        if value != EMPTY:
            continue

        board[index] = COMPUTER
        score = minimax(tuple(board), False)
        board[index] = EMPTY

        if score > best_score:
            best_score = score
            best_move = index

    return best_move


def issue_url(index: int) -> str:
    """Build a pre-filled issue creation URL for one board cell."""
    query = urlencode(
        {
            "title": f"play:{index}",
            "body": "Submit this issue to place your X on the selected Tic-Tac-Toe cell.",
        }
    )
    return f"https://github.com/{USERNAME}/{USERNAME}/issues/new?{query}"


def render_cell(board: list[str], index: int, game_result: str | None) -> str:
    """Render one README table cell."""
    if board[index] != EMPTY:
        return f" **{board[index]}** "
    if game_result:
        return " — "
    return f"[Play]({issue_url(index)})"


def render_game_block(state: dict[str, object]) -> str:
    """Create the markdown game board for README injection."""
    board = state["board"]
    if not isinstance(board, list):
        board = [EMPTY] * 9

    game_result = check_result(board)
    if game_result == "DRAW":
        status_msg = "Game result: draw! Submit any new move after reset to start again."
    elif game_result:
        status_msg = f"Game result: {game_result} wins! Submit any new move after reset to start again."
    else:
        status_msg = "Your move! Click an empty cell to open a pre-filled GitHub Issue."

    return f"""
### 🕹️ Live Community Tic-Tac-Toe
{status_msg}

| | | |
| :---: | :---: | :---: |
| {render_cell(board, 0, game_result)} | {render_cell(board, 1, game_result)} | {render_cell(board, 2, game_result)} |
| {render_cell(board, 3, game_result)} | {render_cell(board, 4, game_result)} | {render_cell(board, 5, game_result)} |
| {render_cell(board, 6, game_result)} | {render_cell(board, 7, game_result)} | {render_cell(board, 8, game_result)} |

_Recruiters and visitors play as **X**. The profile bot answers as **O** using minimax._
"""


def update_readme(state: dict[str, object]) -> None:
    """Replace the README game region with the latest board."""
    content = README_PATH.read_text(encoding="utf-8")
    game_block = render_game_block(state)

    if START_TAG not in content or END_TAG not in content:
        content = f"{content.rstrip()}\n\n{START_TAG}\n{game_block}{END_TAG}\n"
    else:
        before, remainder = content.split(START_TAG, 1)
        _, after = remainder.split(END_TAG, 1)
        content = f"{before}{START_TAG}\n{game_block}{END_TAG}{after}"

    README_PATH.write_text(content, encoding="utf-8")


def play_turn(issue_title: str) -> bool:
    """Apply the human move, compute the bot response, and update files."""
    state = load_state()
    board = state["board"]
    if not isinstance(board, list):
        state = fresh_state()
        board = state["board"]

    move = parse_move(issue_title)
    if move is None or board[move] != EMPTY:
        return False

    board[move] = HUMAN
    game_result = check_result(board)

    if not game_result:
        computer_move = choose_computer_move(board)
        if computer_move is not None:
            board[computer_move] = COMPUTER
        game_result = check_result(board)

    state["status"] = f"GAME_OVER_{game_result}" if game_result else "ONGOING"
    state["turn"] = HUMAN
    save_state(state)
    update_readme(state)
    return True


def main() -> int:
    if "--render" in sys.argv:
        state = load_state()
        save_state(state)
        update_readme(state)
        return 0

    issue_title = os.environ.get("ISSUE_TITLE", "")
    play_turn(issue_title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
