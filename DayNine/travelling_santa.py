import re
from collections import defaultdict
from itertools import permutations

data_re = re.compile(r"^(.*?) to (.*?) = ([0-9]*)$")


def parse_line(line):
    return data_re.match(line).groups()


def build_graph(data):
    g = defaultdict(defaultdict)
    for d in data:
        g[d[0]][d[1]] = int(d[2])
        g[d[1]][d[0]] = int(d[2])
    return g


data = [parse_line(line.strip()) for line in open("input.txt").readlines()]
graph = build_graph(data)
locations = set(graph.keys())
shortest = 100000
longest = 0
for path in permutations(locations):
    journey_length = 0
    for i in range(len(path) - 1):
        journey_length += graph[path[i]][path[i+1]]
    shortest = min(shortest, journey_length)
    longest = max(longest, journey_length)
print(shortest, longest)