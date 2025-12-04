with open("04i.txt") as f:
    rows = [list(i.strip()) for i in f.readlines()]

def remove(rows):
    dirs = [(-1,1),(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    to_remove = []
    for r,row in enumerate(rows):
        for c,val in enumerate(row):
            if val == ".":
                continue
            st = 0
            for dr, dc in dirs:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < len(rows) and 0 <= new_c < len(row):
                    if rows[new_r][new_c] == "@":
                        st += 1
            if st < 4:
                to_remove.append((r,c))
    for p in to_remove:
        rows[p[0]][p[1]] = "."
    return (rows, len(to_remove))

rows, removed = remove(rows)
total = removed

while removed > 0:
    rows, removed = remove(rows)
    total += removed

print(total)
