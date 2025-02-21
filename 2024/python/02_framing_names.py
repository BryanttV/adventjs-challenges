"""02. Framing Names."""


def create_frame(names: list[str]) -> str:
    """
    Create frame.

    Args:
        names (list[str]): List of names to frame

    Returns:
        str: The framed names
    """
    width = len(max(names, key=len)) + 4
    frame = ["*" * width]

    for name in names:
        frame.append(f"* {name.ljust(width - 4, ' ')} *")

    frame.append("*" * width)

    return "\n".join(frame)


print(create_frame(["midu", "madeval", "educalvolpz"]))
# Expected result:
# ***************
# * midu        *
# * madeval     *
# * educalvolpz *
# ***************

print(create_frame(["midu"]))
# Expected result:
# ********
# * midu *
# ********

print(create_frame(["a", "bb", "ccc"]))
# Expected result:
# *******
# * a   *
# * bb  *
# * ccc *
# *******

print(create_frame(["a", "bb", "ccc", "dddd"]))
# Expected result:
# ********
# * a    *
# * bb   *
# * ccc  *
# * dddd *
# ********
