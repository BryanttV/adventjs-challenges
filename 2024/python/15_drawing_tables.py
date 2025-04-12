def draw_table(data: list[dict[str, str | int]]) -> str:
    """Draw table

    Args:
        data (list[dict[str, str  |  int]]): data

    Returns:
        str: table
    """
    headers = list(data[0].keys())

    column_widths = []
    for header in headers:
        column_widths.append(max(len(header), *[len(str(value[header])) for value in data]))

    separator = f'+{"+".join([(width + 2) * "-" for width in column_widths])}+'

    header_row_formatted = []
    for idx, header in enumerate(headers):
        header_row_formatted.append(header.capitalize().ljust(column_widths[idx]))
    header_row_formatted = f'| {" | ".join(header_row_formatted)} |'

    rows = []
    for row in data:
        row_content = [str(row[header]).ljust(column_widths[idx]) for idx, header in enumerate(headers)]
        rows.append(f'| {" | ".join(row_content)} |')

    return "\n".join([separator, header_row_formatted, separator, *rows, separator])


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
