with open("07i.txt") as f:
    lines = [i.strip() for i in f.readlines()]

start_pos = (lines[0].index("S"),0)
grid = [list(l) for l in lines]

def get_split(pos):
    return (pos[0] - 1,pos[1] + 1),(pos[0] + 1,pos[1] + 1)

queue = [start_pos]
visited = []
total = 0

while queue:
    cur = queue.pop(0)
    if cur[1] == len(grid):
        break
    if cur in visited:
        continue
    visited.append(cur)
    if grid[cur[1]][cur[0]] in [".","S"]:
        queue.append((cur[0],cur[1] + 1))
        continue
    left, right = get_split(cur)
    queue.append(left)
    queue.append(right)
    total += 1

print(total)
