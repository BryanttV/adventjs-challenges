"""01. First Gift Repeated!"""


def prepare_gifts(gifts: list) -> list:
    """
    Prepare gifts.

    Returns a new list without duplicates and sorted in ascending order.

    Args:
        gifts (list): The list of gifts to prepare

    Returns:
        list: A list with the prepared gifts
    """
    return sorted(list(set(gifts)))


gifts1 = [3, 1, 2, 3, 4, 2, 5]
prepared_gifts_1 = prepare_gifts(gifts1)
print(prepared_gifts_1)  # [1, 2, 3, 4, 5]

gifts2 = [6, 5, 5, 5, 5]
prepared_gifts_2 = prepare_gifts(gifts2)
print(prepared_gifts_2)  # [5, 6]

gifts3 = []
prepared_gifts_3 = prepare_gifts(gifts3)
print(prepared_gifts_3)  # []
# There are no gifts, the list remains emp
