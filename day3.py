import os
import copy

wires = open(os.path.expanduser("~/Downloads/input.txt")).read().split()

# w1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
# w2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

w1, w2 = wires

wire_1 = [w for w in w1.split(",")]
wire_2 = [w for w in w2.split(",")]

LARGE_MAZE = 20000

maze = [[0 for _ in range(LARGE_MAZE)] for _ in range(LARGE_MAZE)]
start_pos = [LARGE_MAZE // 2, LARGE_MAZE // 2]
cur_pos = copy.deepcopy(start_pos)
wire_len = 0

for w in wire_1:
    direction = w[0]
    amount = int(w[1:])
    for _ in range(amount):
        wire_len += 1
        if direction == "R":
            cur_pos[1] += 1
        elif direction == "L":
            cur_pos[1] -= 1
        elif direction == "D":
            cur_pos[0] += 1
        elif direction == "U":
            cur_pos[0] -= 1
        maze[cur_pos[0]][cur_pos[1]] = wire_len

wire_len = 0
min_dist = float("inf")
cur_pos = copy.deepcopy(start_pos)
for w in wire_2:
    direction = w[0]
    amount = int(w[1:])
    for _ in range(amount):
        wire_len += 1
        if direction == "R":
            cur_pos[1] += 1
        elif direction == "L":
            cur_pos[1] -= 1
        elif direction == "D":
            cur_pos[0] += 1
        elif direction == "U":
            cur_pos[0] -= 1
        if maze[cur_pos[0]][cur_pos[1]] > 0:
            dist = wire_len + maze[cur_pos[0]][cur_pos[1]]
            if dist < min_dist:
                min_dist = dist

print(min_dist)
