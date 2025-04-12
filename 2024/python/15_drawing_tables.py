def draw_table(data: list[dict[str, str | int]]) -> str:
    """Draw table

    Args:
        data (list[dict[str, str  |  int]]): data

    Returns:
        str: table
    """
    content = []
    content.append([column.capitalize() for column in data[0].keys()])
    for row in data:
        temp = []
        for cell in row.values():
            temp.append(cell)
        content.append(temp)
    return content


print(
    draw_table(
        [
            {"name": "Alice", "city": "London"},
            {"name": "Bob", "city": "Paris"},
            {"name": "Charlie", "city": "New York"},
        ]
    )
)
# +---------+-----------+
# | Name    | City      |
# +---------+-----------+
# | Alice   | London    |
# | Bob     | Paris     |
# | Charlie | New York  |
# +---------+-----------+

print(
    draw_table(
        [
            {"gift": "Doll", "quantity": 10},
            {"gift": "Book", "quantity": 5},
            {"gift": "Music CD", "quantity": 1},
        ]
    )
)
# +----------+----------+
# | Gift     | Quantity |
# +----------+----------+
# | Doll     | 10       |
# | Book     | 5        |
# | Music CD | 1        |
# +----------+----------+
