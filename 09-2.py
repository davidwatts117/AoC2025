"""
THIS CODE DOES NOT WORK! I SOLVED THIS WITH DESMOS
"""

with open("09t.txt") as f:
    points = [tuple([int(x) for x in i.strip().split(",")]) for i in f.readlines()]

def get_edge_points(points):
    edge_points = set()
    for i in range(len(points)):
        if points[i - 1][0] == points[i][0]:
            for j in range(min(points[i - 1][1], points[i][1]), max(points[i - 1][1], points[i][1]) + 1):
                edge_points.add((points[i][0], j))
        else:
            for j in range(min(points[i - 1][0], points[i][0]), max(points[i - 1][0], points[i][0]) + 1):
                edge_points.add((j, points[i][1]))
    return edge_points

main_edges = get_edge_points(points)

# get ranges
ranges_by_y = {}
for y in range(9):
    r = []
    in_shape = (0, y) in main_edges
    cur_min = (0 if in_shape else -1)
    for x in range(1, 13):
        if (x, y) in main_edges and (x - 1, y) in main_edges:
            continue
        elif (x, y) in main_edges and not in_shape:
            in_shape = True
            cur_min = x
        elif in_shape and (x, y) in main_edges:
            in_shape = False
            done = False
            for i in range(len(r)):
                if r[i][0] == cur_min:
                    r[i][1] = x
                    done = True
                    break
            if not done:
                r.append([cur_min, x])
            cur_min = -1
        elif (x, y) not in main_edges and (x - 1, y) in main_edges and (x - 2, y) in main_edges:
            done = False
            for i in range(len(r)):
                if r[i][0] == cur_min:
                    r[i][1] = x - 1
                    done = True
                    break
            if not done:
                r.append([cur_min, x - 1])
            cur_min = -1
    ranges_by_y[y] = r

for y, r in ranges_by_y.items():
    print(f"{y}: {r}")
