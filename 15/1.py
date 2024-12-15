ROWS = 50
COLS = 50

grid = [list(input().strip()) for _ in range(ROWS)]

moves = []

input()

dirs = {
    "^": (-1,0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0,-1)
}

pos = [None, None]

for i in range(ROWS):
    for j in range(COLS):
        if grid[i][j] == "@":
            pos = [i, j]


while True:
    try:
        moves += list(input().strip())
    except EOFError:
        break

for move in moves:
    x, y = dirs[move]

    i, j = pos[0], pos[1]

    movable = False

    while True:
        i += x
        j += y

        if grid[i][j] == ".":
            movable = True
            break
        elif grid[i][j] == "#":
            movable = False
            break

    if not movable:
        continue

    while (i, j) != (pos[0], pos[1]):
        grid[i][j] = grid[i-x][j-y]
        i -= x
        j -= y
    
    grid[i][j] = "."

    pos[0] += x
    pos[1] += y

for row in grid:
    print("".join(row))

total = 0

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "O":
            total += 100 * i + j

print(total)
