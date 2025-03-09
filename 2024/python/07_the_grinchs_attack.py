"""Challenge #7: 👹 The Grinch's Attack."""

import re


def fix_packages(packages: str) -> str:
    """Fix Packages.

    Args:
        packages (str): Packages with parentheses

    Returns:
        str: Fixed and sorted packages
    """
    regex = r"\(\w+\)"

    while match := re.search(regex, packages):
        packages = re.sub(regex, match.group()[1:-1][::-1], packages)

    return packages


print(fix_packages("a(cb)de"))
# ➞ "abcde"
# We reverse "cb" inside the parentheses

print(fix_packages("a(bc(def)g)h"))
# ➞ "agdefcbh"
# 1st we reverse "def" → "fed", then we reverse "bcfedg" → "gdefcb"

print(fix_packages("abc(def(gh)i)jk"))
# ➞ "abcighfedjk"
# 1st we reverse "gh" → "hg", then "defhgi" → "ighfed"

print(fix_packages("a(bc(def)g)h"))
# ➞ "acbe"
# 1st we reverse "c" → "c", then "bc" → "cb"
