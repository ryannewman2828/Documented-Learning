#!/usr/bin/python
size = 21


def recurse(x, y):
    global grid
    if x == size - 1:
        if grid[x][y + 1] != 0:
            grid[x][y] = grid[x][y + 1]
            return grid[x][y]
        grid[x][y] = recurse(x, y + 1)
        return grid[x][y]
    elif y == size - 1:
        if grid[x + 1][y] != 0:
            grid[x][y] = grid[x + 1][y]
            return grid[x][y]
        grid[x][y] = recurse(x + 1, y)
        return grid[x][y]
    else:
        if grid[x][y + 1] != 0:
            yPrime = grid[x][y + 1]
        else:
            yPrime = recurse(x, y + 1)
        if grid[x + 1][y] != 0:
            xPrime = grid[x + 1][y]
        else:
            xPrime = recurse(x + 1, y)
        grid[x][y] = xPrime + yPrime
        return grid[x][y]

grid = [0] * size
for i in range(0, size):
    grid[i] = [0] * size

grid[size - 1][size - 2] = 1
grid[size - 2][size - 1] = 1
recurse(0, 0)
print(grid[0][0])
