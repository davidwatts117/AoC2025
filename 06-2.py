with open("06i.txt") as f:
    lines = [line.rstrip("\n") for line in f]

num_lines = lines[:4]
ops = lines[4].replace(" ", "")
ops = list(ops)

cols = list(zip(*num_lines))

blocks = []
i = 0
while i < len(cols):
    col = cols[i]

    if not any(c.isdigit() for c in col):
        i += 1
        continue
\
    start = i
    while i < len(cols) and any(c.isdigit() for c in cols[i]):
        i += 1

    block_cols = cols[start:i]

    block = []
    for col_tuple in block_cols:
        col_digits = []
        for c in col_tuple:
            if c.isdigit():
                col_digits.append(c)
            else:
                col_digits.append("")
        block.append(col_digits)

    blocks.append(block)

final_cols = blocks

total = 0
for op, col in zip(ops, final_cols):
    numbers = []
    for i in range(len(col)):
        while "" in col[i]:
            col[i].remove("")
        numbers.append(int("".join(col[i])))
    if op == "*":
        prod = 1
        for x in numbers:
            prod *= x
        total += prod
    else:
        total += sum(numbers)

print(total)


"""
My plan!
For each column:
- Reverse all nums (str[::-1])
- Add leading characters to retain placement
- List-ify each num and zip them together as follows:

[[123, 45, 6],[328, 64, 98],[51, 387, 215],[64, 23, 314]]
-> [123, 45, 6]
        into
-> [[3,2,1],[5,4,-],[6,-,-]]
        into
-> ([3,5,6],[2,4,-],[6,-,-])
        into
-> (356,24,6)

We will see...
"""
