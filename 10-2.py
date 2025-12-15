"""
WARNING: THIS CODE TAKES F***ING FOREVER TO RUN
"""

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
        
def change_state(state, move):
    new = state.copy()
    for idx in move:
        new[int(idx)] += 1
    return new
    
def valid_state(state, target):
    for i in range(len(state)):
        if state[i] > target[i]:
            return False
    return True
    
def find_shortest(target, moves):
    start = [0 for _ in range(len(target))]
    queue = deque()
    queue.append((start, 0))
    visited = set()
    visited.add(tuple(start))
    int_moves = []
    for m in moves:
        int_moves.append([int(x) for x in m])
    while queue:
        cur, step = queue.popleft()
        if cur == target:
            return (cur, step)
        for move in int_moves:
            new = change_state(cur, move)
            if not valid_state(new, target):
                continue
            t = tuple(new)
            if t not in visited:
                visited.add(t)
                queue.append((new, step + 1))
    return "None found!"
    
total = 0
for i in range(len(jolts)):
    part = find_shortest(jolts[i], moves[i])
    print(f"{i + 1} / {len(jolts)}")
    total += part[1]
print(total)
