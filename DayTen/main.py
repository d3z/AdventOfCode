from look_and_say import parse


def run_n_times(digits, times):
    for i in range(times):
        digits = parse(digits)
    return len(digits)

digits = "1113122113"
print(run_n_times(digits, 40))
print(run_n_times(digits, 50))
