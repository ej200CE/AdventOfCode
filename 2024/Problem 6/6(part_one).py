map = []
directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
turn_right = {'^':'>', '>':'v', 'v':'<', '<':'^'}
visited_positions = set()

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        map.append(line)

# First, find initial position:

found = False
for i, row in enumerate(map):
    for j, col in enumerate(row):
        if col == '^':
            guard_position = (i, j)
            direction = '^'
            found = True
            break
    if found:
        break

while True:
    curr_i, curr_j = guard_position
    di, dj = directions[direction]
    i, j = curr_i + di, curr_j + dj

    if not (0 <= i < len(map) and 0 <= j < len(map[0])):
        break

    if map[i][j] == '#':
        direction = turn_right[direction]
    else:
        visited_positions.add((curr_i, curr_j))
        guard_position = (i, j)

print(len(visited_positions)+1)




