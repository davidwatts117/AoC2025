import math

with open("08i.txt") as f:
    jboxes = [tuple(int(j) for j in i.strip().split(",")) for i in f.readlines()]

def get_dist(p1, p2):
    return float(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2))

def check2(circuits, b1, b2):
    return any(b1 in c and b2 in c for c in circuits)

def check(circuits, b):
    for i, c in enumerate(circuits):
        if b in c:
            return i
    return None

dists = {}
for b1 in jboxes:
    for b2 in jboxes:
        if b1 != b2 and (b1, b2) not in dists and (b2, b1) not in dists:
            dists[get_dist(b1, b2)] = (b1, b2)

dists = dict(sorted(dists.items()))

used_pairs = set()

def get_closest(boxes, circuits):
    for dist, pair in dists.items():
        closest_pair = pair
        del dists[dist]
        break
    return closest_pair[0], closest_pair[1]

circuits = []

for _ in range(1000):
    c1, c2 = get_closest(jboxes, circuits)
    if c1 is None:
        break

    used_pairs.add((c1, c2))

    c1_idx = check(circuits, c1)
    c2_idx = check(circuits, c2)
    
    if c1_idx is None and c2_idx is not None:
        circuits[c2_idx].append(c1)
    
    elif c1_idx is not None and c2_idx is None:
        circuits[c1_idx].append(c2)
    
    elif c1_idx is None and c2_idx is None:
        circuits.append([c1, c2])
    
    elif check2(circuits, c1, c2):
        continue
    
    elif c1_idx != c2_idx:
        if c1_idx < c2_idx:
            circuits[c1_idx].extend(circuits[c2_idx])
            del circuits[c2_idx]
        else:
            circuits[c2_idx].extend(circuits[c1_idx])
            del circuits[c1_idx]

c_lens = []
for c in circuits:
    c_lens.append(len(c))
c_lens.sort()
print(c_lens[-1] * c_lens[-2] * c_lens[-3])
