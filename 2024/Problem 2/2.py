import numpy as np

counter = 0

def safe_check(levels):
    global counter
    all_increasing = all(earlier < later for earlier, later in zip(levels, levels[1:]))
    all_decreasing = all(earlier > later for earlier, later in zip(levels, levels[1:]))
    diffr_matching = all(1 <= abs(earlier - later) <= 3 for earlier, later in zip(levels, levels[1:]))

    if (all_increasing or all_decreasing) and diffr_matching:
        return True


with open("input.txt") as file:
    for line in file:
        levels = [int(x) for x in line.split()]
        if safe_check(levels):
            counter += 1
        else:
            # Part two:
            for i in range(len(levels)):
                new_lvl = np.delete(levels, i)
                if safe_check(new_lvl):
                    counter += 1
                    break

print(counter)