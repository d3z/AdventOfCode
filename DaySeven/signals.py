import re

instruction_re = re.compile(r"(.+) -> (.+)")


def parse_instruction(instruction):
    return instruction_re.match(instruction).groups()


gates = {
    "NOT": lambda x: 65536 + ~x,
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y
}


def calculate(instructions, signals):

    while len(instructions) != 0:

        to_remove = set()
        for instruction in instructions:
            source = instruction[0].split(" ")
            destination = instruction[1]
            if len(source) is 1:
                if source[0].isdigit():
                    signals[destination] = int(source[0])
                    to_remove.add(instruction)
                elif source[0] in signals:
                    signals[destination] = signals[source[0]]
                    to_remove.add(instruction)
            elif len(source) is 2 and source[1] in signals:
                signals[destination] = 65536 + ~signals[source[1]]
                to_remove.add(instruction)
            elif len(source) is 3:
                op1, cmd, op2 = source
                if (op1.isdigit() or op1 in signals) and (op2.isdigit() or op2 in signals):
                    op1 = op1.isdigit() and int(op1) or signals[op1]
                    op2 = op2.isdigit() and int(op2) or signals[op2]
                    signals[destination] = gates[cmd](op1, op2)
                    to_remove.add(instruction)

        instructions = set(instructions) - to_remove

    return signals


def calculate_signals(instructions):
    instructions = list(map(parse_instruction, instructions))
    return calculate(instructions, {})
