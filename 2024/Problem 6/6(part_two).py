map = []
turn_right = {"^":">", ">":"v", "v":"<", "<":"^"}
directions = {"^": (-1,0), ">": (0,1), "v": (1,0), "<": (0,-1)}
original_path = set()
loop_counts = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        map.append(list(line))

found = False
for i, row in enumerate(map):
    for j, col in enumerate(row):
        if col == '^':
            initial_position = (i, j)
            initial_dir = '^'
            found = True
            break
    if found:
        break


guard_position = initial_position
current_dir = initial_dir
while True:
    curr_i, curr_j = guard_position
    di, dj = directions[current_dir]
    i, j = curr_i + di, curr_j + dj

    if not (0 <= i < len(map) and 0 <= j < len(map[0])):
        break

    if map[i][j] == '#':
        current_dir = turn_right[current_dir]
    else:
        original_path.add((i, j))
        guard_position = (i, j)


for (i_0, j_0) in original_path:
    past_states = set()
    map[i_0][j_0] = '#'
    curr_i, curr_j = initial_position
    current_dir = initial_dir
    while True:
        if (curr_i, curr_j, current_dir) in past_states:
            loop_counts += 1
            break   # loop found
        past_states.add((curr_i, curr_j, current_dir))

        di, dj = directions[current_dir]
        i, j = curr_i + di, curr_j + dj

        if not (0 <= i < len(map) and 0 <= j < len(map[0])):
            break   # map escaped

        if map[i][j] == '#':
            current_dir = turn_right[current_dir]
        else:
            curr_i, curr_j = i, j

    map[i_0][j_0] = '.'

print(loop_counts)











