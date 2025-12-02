with open("02i.txt") as f:
    ranges = [i.split("-") for i in f.read().strip().split(",")]

total = 0
for r in ranges:
    for i in range(int(r[0]), int(r[1]) + 1):
        num = str(i)
        done = False
        if len(set(num)) == 1 and len(num) > 1:
            done = True
        else:
            for j in range(2, len(num) + 1):
                if len(num) % j == 0:
                    parts = [num[a:a+j] for a in range(0, len(num), j)]
                    if len(set(parts)) == 1 and len(parts) > 1:
                        done = True
        if done:
            total += i

print(total)
