original_grid = [list(input().strip()) for _ in range(130)]

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

def attempt(i, j):
    
    grid = []
    for row in original_grid:
        grid.append(row.copy())

    if grid[i][j] == "^":
        return False
    
    if grid[i][j] == "#":
        return False
    
    grid[i][j] = "#"
    
    curr = "^"

    r = 59
    c = 62

    cache = set()
    
    while True:

        if (r, c, curr) in cache:
            return True
        
        cache.add((r, c, curr))

        x, y = dirs[curr]

        r += x
        c += y

        if r >= 130 or r < 0 or c >= 130 or c < 0:
            return False

        next_tile = grid[r][c]

        if next_tile != "#":
            continue

        r -= x
        c -= y

        curr = next_dir[curr]


total = 0

for i in range(130):
    for j in range(130):
        if attempt(i, j):
            total += 1

print(total)
