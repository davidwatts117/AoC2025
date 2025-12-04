with open("03i.txt") as f:
    banks = [list(i.strip()) for i in f.readlines()]

def pick_largest_comb(bank):
    result = ""
    start = 0
    for i in range(12):
        rem = 12 - i - 1
        end = len(bank) - rem
        avail = bank[start:end]
        big = max(avail)
        idx = avail.index(big)
        result += big
        start += idx + 1
    return result

total = 0
for bank in banks:
    num_str = pick_largest_comb(bank)
    print(num_str)
    total += int(num_str)

print(total)
