grid = []
count = 0

with open("input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))


for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        diag1 = grid[i-1][j-1] + grid[i][j] + grid[i+1][j+1]
        diag2 = grid[i+1][j-1] + grid[i][j] + grid[i-1][j+1]

        if (diag1 == 'MAS' or diag1 == 'SAM') and (diag2 == 'MAS' or diag2 == 'SAM'):
            count += 1

print(count)

