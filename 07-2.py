with open("07i.txt") as f:
    lines = [i.strip() for i in f.readlines()]

start_pos = (lines[0].index("S"),0)
grid = [list(l) for l in lines]

def get_split(pos):
    return (pos[0] - 1,pos[1] + 1),(pos[0] + 1,pos[1] + 1)

h = len(grid)
w = len(grid[0])

ways = [[0]*w for _ in range(h)]
ways[start_pos[1]][start_pos[0]] = 1

for y in range(h - 1):
    for x in range(w):
        if ways[y][x] == 0:
            continue
        cur = (x,y)
        cell = grid[cur[1]][cur[0]]
        if cell in [".","S"]:
            nx, ny = cur[0],cur[1] + 1
            if 0 <= nx < w:
                ways[ny][nx] += ways[y][x]
            continue
        left, right = get_split(cur)
        if 0 <= left[0] < w:
            ways[left[1]][left[0]] += ways[y][x]
        if 0 <= right[0] < w:
            ways[right[1]][right[0]] += ways[y][x]

total = 0
for x in range(w):
    total += ways[h - 1][x]

print(str(total))

#10357305916520
