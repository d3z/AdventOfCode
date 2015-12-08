def count_chars(strings):
    total = 0
    for s in strings:
        print(s.encode("unicode-escape"))
        print(s)
        total += (len(s.encode("unicode-escape")) - len(s))
    return total

print(count_chars([s.strip() for s in open("input.txt").readlines()]))