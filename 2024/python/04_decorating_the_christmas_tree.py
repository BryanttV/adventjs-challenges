"""Challenge #4: 🎄Decorating The Christmas Tree."""


def create_xmas_tree(height: int, ornament: str) -> str:
    """
    Create christmas tree.

    Args:
      height (int): Height of the tree
      ornament (str): Symbol to draw

    Returns:
        str: Drawn tree
    """
    width = height * 2 - 1
    xmas_tree = [(ornament * i).center(width, "_") for i in range(1, width + 1, 2)]

    # Add the trunk
    trunk_part = "#".center(width, "_")
    xmas_tree.extend([trunk_part] * 2)

    return "\n".join(xmas_tree)


print(create_xmas_tree(5, "*"))
# ____*____
# ___***___
# __*****__
# _*******_
# *********
# ____#____
# ____#____

print(create_xmas_tree(3, "+"))
# __+__
# _+++_
# +++++
# __#__
# __#__

print(create_xmas_tree(6, "@"))
# _____@_____
# ____@@@____
# ___@@@@@___
# __@@@@@@@__
# _@@@@@@@@@_
# @@@@@@@@@@@
# _____#_____
# _____#_____
