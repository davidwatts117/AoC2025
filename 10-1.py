from collections import deque
import copy

with open("10i.txt") as f:
    problems = [i.strip().split("  ") for i in f.readlines()]
    goals = []
    moves = []
    jolts = []
    for p in problems:
        goals.append(list(p[0]))
        moves.append([i.split(",") for i in p[1].split(" ")])
        jolts.append([int(i) for i in p[2].split(",")]) 


def change_state(state_list, move):
    for idx in move:
        i = int(idx)
        if state_list[i] == "#":
            state_list[i] = "."
        else:
            state_list[i] = "#"
    return state_list

def find_shortest(goal, moves):
    start = ["0" for _ in range(len(goal))]
    start_string = "".join(start)

    queue = deque()
    queue.append((start_string, 0))

    visited = set()
    visited.add(start_string)

    goal_string = "".join(goal)

    int_moves = []
    for m in moves:
        int_moves.append([int(x) for x in m])

    while queue:
        cur_string, step = queue.popleft()
        cur_list = list(cur_string)

        for move in int_moves:
            new_list = cur_list.copy()
            new_list = change_state(new_list, move)

            new_string = "".join(new_list)

            if new_string == goal_string:
                return (new_list, step + 1)

            if new_string not in visited:
                visited.add(new_string)
                queue.append((new_string, step + 1))

    return "None found!"


total = 0
for i in range(len(goals)):
    part = find_shortest(goals[i], moves[i])
    print(f"{i + 1} / {len(goals)}")
    total += part[1]

print(total)
