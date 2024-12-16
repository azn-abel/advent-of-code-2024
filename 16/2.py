import sys

sys.setrecursionlimit(100000)

grid = []

while True:
    try:
        grid.append(list(input().strip()))
    except EOFError:
        break

pos = None
end = None

dirs = [(0, 1),(0,-1),(1, 0),(-1,0)]

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "S":
            pos = (i, j)
        elif val == "E":
            end = (i, j)

import collections


def bfs(grid, pos):
    cache = {}

    q = collections.deque([(pos, (0, 1), 0, set())])

    cache[(pos, (0, 1))] = 0

    seats = set()

    min_path = float("inf")

    while q:
        (i, j), dir, curr, path = q.popleft()

        if ((i, j), dir) in cache and curr > cache[((i, j), dir)]:
            continue

        cache[((i, j), dir)] = curr

        for d in dirs:
            di, dj = d
            i2, j2 = i + di, j + dj

            if (i2, j2) in path:
                continue

            if ((i2, j2), d) in cache:
                temp = cache[((i2, j2), d)]
                if d == dir:
                    if curr + 1 < temp:
                        cache[(i2, j2)] = curr + 1
                    q.append(((i2, j2), d, curr + 1, path | {(i, j)}))
                else:
                    if curr + 1001 < temp:
                        cache[(i2, j2)] = curr + 1001
                    q.append(((i2, j2), d, curr + 1001, path | {(i, j)}))
                continue

            if grid[i2][j2] == "E":
                if curr + 1 < min_path:
                    min_path = curr + 1
                    seats = path | {(i, j), (i2, j2)}
                elif curr + 1 == min_path:
                    seats.update(path | {(i, j), (i2, j2)})
                continue

            if grid[i2][j2] != ".":
                continue

            if d == dir:
                q.append(((i2, j2), d, curr + 1, path | {(i, j)}))
            else:
                q.append(((i2, j2), d, curr + 1001, path | {(i, j)}))

    return min_path, seats
                
min_path, seats = bfs(grid, pos)

for i, j in seats:
    grid[i][j] = "O"

with open("output.txt", "w") as file:
    for row in grid:
        line = "".join(row)
        file.write(line + "\n")
    

count = 0

for row in grid:
    for val in row:
        if val == "O":
            count += 1

print(min_path, count)
