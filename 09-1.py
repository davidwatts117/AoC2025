with open("09i.txt") as f:
    points = [[int(x) for x in i.strip().split(",")] for i in f.readlines()]

best_area = 0

for i in range(len(points)):
    x1, y1 = points[i]
    for j in range(i + 1, len(points)):
        x2, y2 = points[j]
        area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
        if area > best_area:
            best_area = area

print(best_area)
