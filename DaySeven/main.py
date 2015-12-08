from signals import calculate_signals


instructions = [line.strip() for line in open("input.txt").readlines()]

signals = calculate_signals(instructions)
print(signals["a"])
