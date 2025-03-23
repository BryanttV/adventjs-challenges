"""Challenge #12: 💵 How Much Does The Tree Cost?"""


def calculate_price(ornaments: str) -> int | None:
    """Calculate the total value of a Christmas tree based on its ornaments.

    Args:
        ornaments (str): A string representing the ornaments on the tree.

    Returns:
        int: The calculated tree value or None if an invalid character is present.
    """
    values = {"*": 1, "o": 5, "^": 10, "#": 50, "@": 100}
    total = 0
    prev_value = 0

    for ornament in reversed(ornaments):
        if ornament not in values:
            return None
        value = values[ornament]
        total += -value if value < prev_value else value
        prev_value = value

    return total


print(calculate_price("***"))  # 3 (1 + 1 + 1)
print(calculate_price("*o"))  # 4 (5 - 1)
print(calculate_price("o*"))  # 6 (5 + 1)
print(calculate_price("*o*"))  # 5 (-1 + 5 + 1)
print(calculate_price("**o*"))  # 6 (1 - 1 + 5 + 1)
print(calculate_price("o***"))  # 8 (5 + 3)
print(calculate_price("*o@"))  # 94 (-5 - 1 + 100)
print(calculate_price("*#"))  # 49 (-1 + 50)
print(calculate_price("@@@"))  # 300 (100 + 100 + 100)
print(calculate_price("#@"))  # 50 (-50 + 100)
print(calculate_price("#@Z"))  # undefined (Z is unknown)
