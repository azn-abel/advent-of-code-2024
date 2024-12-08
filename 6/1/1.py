grid = [list(input().strip()) for _ in range(130)]

r = 59
c = 62

curr = "^"

dirs = {
    "^": (-1,0),
    ">": (0,1),
    "<": (0,-1),
    "v": (1,0)
}

next_dir = {
    "^": ">",
    ">": "v",
    "<": "^",
    "v": "<"
}

total = 1

while True:
    x, y = dirs[curr]

    r += x
    c += y

    if r >= 130 or r < 0 or c >= 130 or c < 0:
        break

    next_tile = grid[r][c]

    if next_tile == ".":
        grid[r][c] = "X"
        total += 1
        continue

    if next_tile == "X":
        continue

    r -= x
    c -= y

    curr = next_dir[curr]


print(total)
