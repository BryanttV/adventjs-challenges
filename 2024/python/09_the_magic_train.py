"""Challenge #9: 🚂 The Magic Train."""

from typing import Literal

Result = Literal["none", "crash", "eat"]
Direction = Literal["U", "D", "R", "L"]


def move_train(board: list[str], mov: Direction) -> Result:
    """
    Move train.

    Args:
        board (list[str]): Represent the train situation
        mov (Direction): Movement direction
            - "U: Up
            - "D: Down
            - "R: Right
            - "L: Left

    Returns:
        Result:
            - "none": Train moved successfully, no collision or food eaten
            - "crash": Train collided with itself or a wall
            - "eat": Train ate a food item
    """
    width = len(board[0]) - 1
    height = len(board) - 1
    mapping: dict[str, Result] = {
        "o": "crash",
        "*": "eat",
        "·": "none",
    }

    for index, line in enumerate(board):
        if line.count("@"):
            position = line.index("@")
            directions = {
                "U": board[index - 1][position] if index > 0 else "o",
                "D": board[index + 1][position] if index < height else "o",
                "R": line[position + 1] if position < width else "o",
                "L": line[position - 1] if position > 0 else "o",
            }
            return mapping[directions[mov]]

    return "none"


sample_board = [
    "·····",
    "*····",
    "@····",
    "o····",
    "o····",
]

print(move_train(sample_board, "U"))
# ➞ 'eat'
# Because the train moves up and finds a magical fruit

print(move_train(sample_board, "D"))
# ➞ 'crash'
# The train moves down and the head crashes into itself

print(move_train(sample_board, "L"))
# ➞ 'crash'
# The train moves to the left and crashes into the wall

print(move_train(sample_board, "R"))
# ➞ 'none'
# The train moves to the right and there is empty space on the right
