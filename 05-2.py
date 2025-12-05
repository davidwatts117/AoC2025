with open("05i.txt") as f:
    stuff = f.read().strip().split("\n")
    ranges = [[int(x) for x in line.split("-")] for line in stuff]

ranges.sort()

merged = [ranges[0]]
for start, end in ranges[1:]:
    last_start, last_end = merged[-1]
    if start <= last_end + 1:
        merged[-1][1] = max(last_end, end)
    else:
        merged.append([start, end])

total = sum(end - start + 1 for start, end in merged)
print(total)


# 400221822437275 too high
