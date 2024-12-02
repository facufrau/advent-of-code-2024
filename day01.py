# --- Day 1: Historian Hysteria ---

with open("input01.txt") as file:
    left = []
    right = []
    for line in file:
        itemleft, itemright = (int(x) for x in line.strip().split())
        left.append(itemleft)
        right.append(itemright)

    left_sorted = sorted(left)
    right_sorted = sorted(right)

# Part one
distance = 0
for l, r in zip(left_sorted, right_sorted):
    distance += abs(l-r)
print(f"Part one answer -->  {distance}")

# Part two
similarity = sum(right.count(num) * num for num in left)
print(f"Part two answer -->  {similarity}")