"""Challenge #11: 🏴‍☠️ Filenames encoded."""

import re

def decode_filename(filename: str) -> str:
  """Decode filename.

  Args:
      filename (str): The filename

  Returns:
      str: The decoded filename
  """
  return re.search(r"(\d+)_([a-zA-Z_-]+.\w+)", filename).group(2)


print(decode_filename('2023122512345678_sleighDesign.png.grinchwa')) # "sleighDesign.png"

print(decode_filename('42_chimney_dimensions.pdf.hack2023')) # "chimney_dimensions.pdf"

print(decode_filename('987654321_elf-roster.csv.tempfile')) # "elf-roster.csv"
