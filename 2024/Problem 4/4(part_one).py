grid = []
count = 0

with open("input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        #check to the right:
        if j <= len(grid[0]) - 4:
            if grid[i][j] == 'X' and grid[i][j+1] == 'M' and grid[i][j+2] == 'A' and grid[i][j+3] == 'S':
                count += 1
        #check to the left:
        if j >= 3:
            if grid[i][j] == 'X' and grid[i][j-1] == 'M' and grid[i][j-2] == 'A' and grid[i][j-3] == 'S':
                count += 1
        #check down:
        if i <= len(grid) - 4:
            if grid[i][j] == 'X' and grid[i+1][j] == 'M' and grid[i+2][j] == 'A' and grid[i+3][j] == 'S':
                count += 1
        #check up:
        if i >= 3:
            if grid[i][j] == 'X' and grid[i-1][j] == 'M' and grid[i-2][j] == 'A' and grid[i-3][j] == 'S':
                count += 1
        #check up-right diagonal:
        if i >= 3 and j <= len(grid[0]) - 4:
            if grid[i][j] == 'X' and grid[i-1][j+1] == 'M' and grid[i-2][j+2] == 'A' and grid[i-3][j+3] == 'S':
                count += 1
        #check up-left diagonal:
        if i >= 3 and j >= 3:
            if grid[i][j] == 'X' and grid[i-1][j-1] == 'M' and grid[i-2][j-2] == 'A' and grid[i-3][j-3] == 'S':
                count += 1
        #check down-right diagonal:
        if i <= len(grid) - 4 and j <= len(grid[0]) - 4:
            if grid[i][j] == 'X' and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A' and grid[i+3][j+3] == 'S':
                count += 1
        #check down-left diagonal:
        if i <= len(grid) - 4 and j >= 3:
            if grid[i][j] == 'X' and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A' and grid[i+3][j-3] == 'S':
                count += 1

print(count)