with open("02i.txt") as f:
    ranges = [i.split("-") for i in f.read().strip().split(",")]

total = 0
for r in ranges:
    for i in range(int(r[0]),int(r[1]) + 1):
        num = str(i)
        if num[len(num) // 2:] == num[0:len(num) // 2]:
            total += i

print(total)
