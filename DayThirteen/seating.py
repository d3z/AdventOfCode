from itertools import permutations

guests = set(["me"])


def parse_row(row):
    global guests
    row_parts = row.split()
    guest1 = row_parts[0]
    gol = row_parts[2]
    units = int(row_parts[3])
    guest2 = row_parts[10][:-1]
    guests.add(guest1)
    guests.add(guest2)
    return guest1, guest2, (gol == "gain") and units or -units


guest_relations = [r for r in map(parse_row, open("input.txt").readlines())]

seatings = permutations(guests)

highest_happiness = 0

for seating in seatings:
    total = 0
    for i in range(-1, len(seating) - 1):
        guest1 = seating[i]
        guest2 = seating[i + 1]
        if "me" in (guest1, guest2):
            continue
        total += [u for g1, g2, u in guest_relations if g1 == guest1 and g2 == guest2][0]
        total += [u for g1, g2, u in guest_relations if g1 == guest2 and g2 == guest1][0]
    highest_happiness = max(highest_happiness, total)

print(highest_happiness)
