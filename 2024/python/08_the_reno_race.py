"""Challenge #8: 🦌 The Reno Race."""


def draw_race(indices: list[int], length: int) -> str:
    """
    Draw race.

    Args:
        indices (list[int]):The reno indices
        length (int): The length of the race

    Returns:
        str: The reno race
    """
    reno_race = []
    for idx, progress in enumerate(indices, 1):
        line = ["~"] * length
        if progress != 0:
            position = progress if progress > 0 else length + progress
            line[position] = "r"
        spaces = len(indices) - idx
        reno_race.append(spaces * " " + "".join(line) + f" /{idx}")

    return "\n".join(reno_race)


print(draw_race([0, 5, -3], 10))
#   ~~~~~~~~~~ /1
#  ~~~~~r~~~~ /2
# ~~~~~~~r~~ /3
#   ~~~~~~~~~~ /1
#  ~~~~~r~~~~ /2
# ~~~~~~~r~~ /3

print(draw_race([2, -1, 0, 5], 8))
#    ~~r~~~~~ /1
#   ~~~~~~~r /2
#  ~~~~~~~~ /3
# ~~~~~r~~ /4

print(draw_race([3, 7, -2], 12))
#   ~~~r~~~~~~~~ /1
#  ~~~~~~~r~~~~ /2
# ~~~~~~~~~~r~ /3
