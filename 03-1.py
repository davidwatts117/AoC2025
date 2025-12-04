with open("03i.txt") as f:
    banks = [list(i.strip()) for i in f.readlines()]

total = 0
for bank in banks:
    highest = 0
    high_idx = 0
    for i in range(len(bank) - 1):
        if int(bank[i]) > highest:
            highest = int(bank[i])
            high_idx = i
    second = 0
    for i in range(high_idx + 1, len(bank)):
        if int(bank[i]) > second:
            second = int(bank[i])
    total += int(str(highest) + str(second))

print(total)
