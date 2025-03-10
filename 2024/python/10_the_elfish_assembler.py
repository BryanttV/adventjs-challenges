"""Challenge #10: 👩‍💻 The Elfish Assembler."""

from collections import defaultdict


def _compile(instructions: list[str]) -> int | None:
    """
    Compile

    Args:
        instructions (list[str]): The instructions to execute

    Returns:
        int | None: The value of the register A
    """
    result = defaultdict(int)

    idx = 0
    while idx < len(instructions):
        values = instructions[idx].split(" ")
        action = values[0]
        if action == "MOV":
            result[values[2]] = result.get(values[1], None) or int(values[1])
        elif action == "INC":
            result[values[1]] += 1
        elif action == "DEC":
            result[values[1]] -= 1
        elif action == "JMP":
            if result[values[1]] == 0:
                idx = int(values[2])
                continue

        idx += 1

    return result.get("A", None)


instructions_sample = [
    "MOV -1 C",  # copies -1 to register 'C',
    "INC C",  # increments the value of register 'C'
    "JMP C 1",  # jumps to the instruction at index 1 if 'C' is 0
    "MOV C A",  # copies register 'C' to register 'A',
    "INC A",  # increments the value of register 'A'
]

print(_compile(instructions_sample))  # -> 2
#  Step-by-step execution:
#  0: MOV -1 C -> The register C receives the value -1
#  1: INC C    -> The register C becomes 0
#  2: JMP C 1  -> C is 0, jumps to the instruction at index 1
#  1: INC C    -> The register C becomes 1
#  2: JMP C 1  -> C is 1, the instruction is ignored
#  3: MOV C A  -> Copies register C to A. Now A is 1
#  4: INC A    -> The register A becomes 2
