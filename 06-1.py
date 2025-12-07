with open("06i.txt") as f:
    things = [line.strip() for line in f]

nums = [line.split() for line in things[:4]]
ops  = things[4].split()

cols = list(zip(*nums))

total = 0
for op, col in zip(ops, cols):
    numbers = [int(x) for x in col]
    if op == "*":
        p = 1
        for x in numbers:
            p *= x
        total += p
    else:
        total += sum(numbers)

print(total)
