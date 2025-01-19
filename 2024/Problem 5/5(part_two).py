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
    was_correct = True
    while True:
        is_correct = True
        position = {page: idx for idx, page in enumerate(update)}
        for X, Y in rules:
            if X in position and Y in position:
                if position[X] > position[Y]:
                    was_correct = False
                    is_correct = False
                    update[position[X]], update[position[Y]] = update[position[Y]], update[position[X]]
                    break

        if is_correct:
            break

    if not was_correct:
        summ += update[len(update)//2]

print(summ)