import re

instruction_re = re.compile(r"^(toggle|turn off|turn on) (\d+?),(\d+?) through (\d+?),(\d+?)$")

digial_commands = {
    "toggle": lambda x: not x,
    "turn on": lambda x: True,
    "turn off": lambda x: False
}

analog_commands = {
    "toggle": lambda x: x + 2,
    "turn on": lambda x: x + 1,
    "turn off": lambda x: x - 1 is not -1 and x - 1 or 0
}


def follow_instruction(instruction, lights, commands):
    command, x1, y1, x2, y2 = instruction_re.match(instruction).groups()
    for a in range(int(x1), int(x2) + 1):
        for b in range(int(y1), int(y2) + 1):
            lights[a][b] = commands[command](lights[a][b])
    return lights


def follow_instructions(instructions, lights, commands):
    for line in [line.strip() for line in open("input.txt").readlines()]:
        lights = follow_instruction(line, lights, commands)
    return lights


def count_lights_on(lights):
    count = 0
    for row in lights:
        count += len(list(filter(lambda x: x is True, row)))
    return count


def calculate_brightness(lights):
    total = 0
    for row in lights:
        for light in row:
            total += light
    return total


instructions = [line.strip() for line in open("input.txt").readlines()]


lights = [[False for x in range(1000)] for y in range(1000)]
print(count_lights_on(follow_instructions(instructions, lights, digial_commands)))

lights = [[0 for x in range(1000)] for y in range(1000)]
print(calculate_brightness(follow_instructions(instructions, lights, analog_commands)))