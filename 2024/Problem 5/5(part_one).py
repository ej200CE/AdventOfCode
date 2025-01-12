rules = set()
updates = []
summ = 0

with open("input.txt") as file:
    parcing_rule = True
    for line in file:
        line = line.strip()
        if not line:
            parcing_rule = False
            continue
        if parcing_rule:
            rules.add(tuple(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))


for update in updates:
    position = {page: idx for idx, page in enumerate(update)}
    rules_valid = True
    for X, Y in rules:
        if X in position and Y in position:
            if position[X] >= position[Y]:
                rules_valid = False
                break

    if rules_valid:
        summ += update[len(update) // 2]

print(summ)

