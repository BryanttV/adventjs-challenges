"""Challenge #6: 📦 Is The Gift Inside The Box?"""


def in_box(box: list[str]) -> bool:
    """
    In Box.

    Args:
        box (list[str]): The box to check

    Returns:
        bool: True if the gift is inside the box
    """
    box = box[1:-1]

    for line in box:
        if "*" in line and line.index("*") > 0 and line.index("*") < len(line) - 1:
            return True

    return False


print(
    in_box(
        [
            "###",
            "#*#",
            "###",
        ]
    )
)  # True

print(
    in_box(
        [
            "####",
            "#*#",
            "##",
            "####",
        ]
    )
)  # True

print(
    in_box(
        [
            "#####",
            "##",
            "##*",
            "#####",
        ]
    )
)  # False

print(
    in_box(
        [
            "#####",
            "#   #",
            "#   #",
            "#   #",
            "#####",
        ]
    )
)  # False
