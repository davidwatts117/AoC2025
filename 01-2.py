with open("01i.txt") as f:
    lines = [i.strip() for i in f.readlines()]

cur_ori = 50
pw = 0
for line in lines:
    prev_ori = cur_ori
    if line[0] == "L":
        cur_ori -= int(line[1:])
    if line[0] == "R":
        cur_ori += int(line[1:])
    while cur_ori > 100:
        cur_ori -= 100
        pw += 1
    while cur_ori < -100:
        cur_ori += 100
        pw += 1
    if cur_ori < 0 and prev_ori != 0:
        pw += 1
    cur_ori %= 100
    if cur_ori == 0:
        pw += 1

print(pw)
