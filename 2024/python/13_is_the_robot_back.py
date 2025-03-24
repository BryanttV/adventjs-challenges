"""Challenge #13: 🤖 Is The Robot Back?"""


def is_robot_back(moves: str) -> bool | list[int]:
    """
    Is robot back.

    Args:
        moves (str): moves

    Returns:
        bool | list[int]: Return true if robot returns or position
    """
    pairs = {"R": "L", "L": "R", "U": "D", "D": "U"}
    moves_list = list(moves)
    x = 0
    y = 0

    final_moves = []
    index = 0
    while index < len(moves_list):
        move = moves_list[index]
        if move == "*":
            final_moves.append(moves_list[index + 1])
        elif move == "!":
            final_moves.append(pairs[moves_list.pop(index + 1)])
        elif move == "?":
            next_value = moves_list.pop(index + 1)
            if next_value not in final_moves:
                final_moves.append(next_value)
        else:
            final_moves.append(move)
        index += 1

    for move in final_moves:
        if move == "R":
            x += 1
        elif move == "L":
            x -= 1
        elif move == "U":
            y += 1
        elif move == "D":
            y -= 1

    return [x, y] if x or y else True


print(is_robot_back("LLL!R"))  # [1, 0]
print(is_robot_back("R"))  # [1, 0]
print(is_robot_back("RL"))  # true
print(is_robot_back("RLUD"))  # true
print(is_robot_back("*RU"))  # [2, 1]
print(is_robot_back("R*U"))  # [1, 2]
print(is_robot_back("LLL!R"))  # [-4, 0]
print(is_robot_back("R?R"))  # [1, 0]
print(is_robot_back("U?D"))  # true
print(is_robot_back("R!L"))  # [2, 0]
print(is_robot_back("U!D"))  # [0, 2]
print(is_robot_back("R?L"))  # true
print(is_robot_back("U?U"))  # [0, 1]
print(is_robot_back("*U?U"))  # [0, 2]
print(is_robot_back("U?D?U"))  # true

# Step-by-step examples:
print(is_robot_back("R!U?U"))  # [1, 0]
# 'R'  -> moves to the right
# '!U' -> inverts and becomes 'D'
# '?U' -> moves upwards, because the 'U' movement hasn't been done yet

print(is_robot_back("UU!U?D"))  # [0, 1]
# 'U'  -> moves upwards
# 'U'  -> moves upwards
# '!U' -> inverts and becomes 'D'
# '?D' -> does not move, since the 'D' movement has already been done
