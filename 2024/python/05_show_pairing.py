"""05. Show Pairing."""

from collections import defaultdict
from typing import TypedDict


class Boot(TypedDict):
    """Boot dict"""

    type: str
    size: int


def organize_shoes(shoes: list[Boot]) -> list[int]:
    """
    Organize shoes.

    Args:
        shoes (list[Boot]): Shoes

    Returns:
        list[int]: Available shoes
    """
    boots_count = defaultdict(lambda: {"I": 0, "R": 0})

    for boot in shoes:
        boots_count[boot["size"]][boot["type"]] += 1

    result = []
    for size, counts in boots_count.items():
        pairs = min(counts["I"], counts["R"])
        result.extend([size] * pairs)

    return result


shoes1: list[Boot] = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
    {"type": "R", "size": 42},
    {"type": "I", "size": 41},
    {"type": "I", "size": 42},
]
print(organize_shoes(shoes1))
# [38, 42]

shoes2: list[Boot] = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
    {"type": "I", "size": 38},
    {"type": "I", "size": 38},
    {"type": "R", "size": 38},
]
print(organize_shoes(shoes2))
# [38, 38]

shoes3: list[Boot] = [
    {"type": "I", "size": 38},
    {"type": "R", "size": 36},
    {"type": "R", "size": 42},
    {"type": "I", "size": 41},
    {"type": "I", "size": 43},
]
print(organize_shoes(shoes3))
# []
