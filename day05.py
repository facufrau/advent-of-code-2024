# --- Day 5: Print Queue ---

with open("input05.txt") as file:
    rules = {}
    pages_updates = []
    for line in file:
        line = line.strip()
        if "|" in line:
            n1, n2 = eval(line.replace("|", ","))
            if n1 not in rules:
                rules[n1] = [n2,]
            else:
                rules[n1].append(n2)
        elif "," in line:
            pages_updates.append([int(x) for x in line.strip().split(",")])

# Part one
total = 0
incorrects = []  # For part two
for page in pages_updates:
    checks = []
    for i, p in enumerate(page):
        if p not in rules:
            rules[p] = []
        else:
            checks.append(all(x in rules[p] for x in page[i+1:]))
    if all(checks):
        total += page[len(page)//2]
    else: # For part two
        incorrects.append(page)
print(f"Part one answer --> {total}")

# Part two
def check_order(page1, page2, rules):
    return page2 in rules[page1]

def order_update(item, rules):
    changed = True
    while changed:
        changed = False
        for i in range(len(item)-1):
            if not check_order(item[i], item[i+1], rules):
                item[i], item[i+1] = item[i+1], item[i]
                changed = True
    return item

for wrong_update in incorrects:
    order_update(wrong_update, rules)
total = sum(x[len(x)//2] for x in incorrects)
print(f"Part one answer --> {total}")

