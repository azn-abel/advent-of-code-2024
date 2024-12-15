ROWS = 50
COLS = 100

grid = []

for _ in range(ROWS):
    line = input().strip()
    row = []

    for char in line:
        if char == "@":
            row += [char, "."]
        elif char == "O":
            row += ["[", "]"]
        else:
            row += [char, char]

    grid.append(row)

input()

def can_move_ud(mi, i, j, all):

    if grid[i][j] == ".":
        return True
    if grid[i][j] == "#":
        return False
    
    if grid[i][j] == "[":
        right = can_move_ud(mi, i+mi, j+1, all)
        left = can_move_ud(mi, i+mi, j, all)
        all.add((i, j))
        all.add((i, j+1))
        return left and right
    elif grid[i][j] == "]":
        left = can_move_ud(mi, i+mi, j-1, all)
        right = can_move_ud(mi, i+mi, j, all)
        all.add((i, j))
        all.add((i, j-1))
        return left and right


def move_ud(mi, pos, all):

    mapping = {}

    for i, j in all:
        mapping[(i+mi, j)] = grid[i][j]
        grid[i][j] = "."
    for (i, j), val in mapping.items():
        grid[i][j] = val

    grid[pos[0]][pos[1]] = "."
    pos[0] += mi
    grid[pos[0]][pos[1]] = "@"


def move_lr(m, pos, i, j):
    mi, mj = dirs[m]
    i, j = pos
    
    while True:
        i += mi
        j += mj

        if grid[i][j] == ".":
            break
        elif grid[i][j] == "#":
            return
        
    while (i, j) != (pos[0], pos[1]):
        grid[i][j] = grid[i-mi][j-mj]
        i -= mi
        j -= mj
        
    grid[i][j] = "."

    pos[0] += mi
    pos[1] += mj


moves = []

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

for m in moves:
    mi, _ = dirs[m]

    i, j = pos

    if mi == 0:
        move_lr(m, pos, i, j)
    else:
        all = set()
        if can_move_ud(mi, i+mi, j, all):
            move_ud(mi, pos, all)

total = 0

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val == "[":
            total += 100 * i + j

print(total)
