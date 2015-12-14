import re


class Reindeer(object):
    def __init__(self, name, speed, run_duration, rest_duration):
        self.name = name
        self.speed = speed
        self.run_duration = run_duration
        self.rest_duration = rest_duration
        self.distance = 0
        self.running = True
        self.current_state = self.run_duration
        self.score = 0

    def tick(self):
        if self.running:
            self.distance += self.speed
        self.current_state -= 1
        if self.current_state == 0:
            if self.running:
                self.current_state = self.rest_duration
                self.running = False
            else:
                self.current_state = self.run_duration
                self.running = True

reindeer_re = re.compile(r"^(.*?) can fly ([0-9]*) km/s for ([0-9]*) seconds, but then must rest for ([0-9]*) seconds.$")
reindeer = []

for line in open("input.txt").readlines():
    name, speed, duration, rest = reindeer_re.match(line).groups()
    reindeer.append(Reindeer(name, int(speed), int(duration), int(rest)))

for i in range(2504):
    for r in reindeer:
        r.tick()
    reindeer.sort(key=lambda r: r.distance, reverse=True)
    for r in reindeer:
        if r.distance == reindeer[0].distance:
            r.score += 1

winner_by_distance = reindeer[0]
print(winner_by_distance.name, winner_by_distance.distance)

reindeer.sort(key=lambda r: r.score, reverse=True)
winner_by_score = reindeer[0]
print(winner_by_score.name, winner_by_score.score)