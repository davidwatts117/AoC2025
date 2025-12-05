with open("05t.txt") as f:
    ranges, loaves = f.read().strip().split("\n\n")
    ranges = [i.strip().split("-") for i in ranges.split("\n")]
    loaves = [int(i) for i in loaves.strip().split("\n")]

total = 0
for loaf in loaves:
    for r in ranges:
        if loaf >= int(r[0]) and loaf <= int(r[1]):
            total += 1
            break

print(total)
