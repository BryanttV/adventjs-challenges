"""03. Organizing The Inventory."""


def organize_inventory(
    inventory: list[dict[str, str | int]],
) -> dict[str, dict[str, int]]:
    """
    Organize inventory.

    Args:
        inventory (list[dict[str, str  |  int]]): The inventory

    Returns:
        dict[str, dict[str, int]]: Organized inventory
    """
    organized_inventory = {}

    for obj in inventory:
        category = obj["category"]
        quantity = obj["quantity"]
        name = obj["name"]

        if category in organized_inventory:
            if name in organized_inventory[category]:
                organized_inventory[category][name] += quantity
            else:
                organized_inventory[category][name] = quantity
        else:
            organized_inventory[category] = {name: quantity}

    return dict(organized_inventory)


test_inventory1 = [
    {"name": "doll", "quantity": 5, "category": "toys"},
    {"name": "car", "quantity": 3, "category": "toys"},
    {"name": "ball", "quantity": 2, "category": "sports"},
    {"name": "car", "quantity": 2, "category": "toys"},
    {"name": "racket", "quantity": 4, "category": "sports"},
]

print(organize_inventory(test_inventory1))
# Expected result:
# {
#   toys: {
#     doll: 5,
#     car: 5
#   },
#   sports: {
#     ball: 2,
#     racket: 4
#   }

test_inventory2 = [
    {"name": "book", "quantity": 10, "category": "education"},
    {"name": "book", "quantity": 5, "category": "education"},
    {"name": "paint", "quantity": 3, "category": "art"},
]

print(organize_inventory(test_inventory2))
# Expected result:
# {
#   education: {
#     book: 15
#   },
#   art: {
#     paint: 3
#   }
# }
