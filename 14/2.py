COLS = 101
ROWS = 103

INPUT_SIZE = 500

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

robots = []

for _ in range(INPUT_SIZE):
    pv = input().strip().split()
    x, y = tuple(int(x) for x in pv[0][2:].split(","))
    v = tuple(int(x) for x in pv[1][2:].split(","))

    robots.append([x, y, v])

    grid[y][x] += 1 


for i in range(10000):
    search = False

    for r in robots:
        x, y, v = r
        new_x = (x + v[0]) % COLS
        new_y = (y + v[1]) % ROWS

        grid[y][x] -= 1
        grid[new_y][new_x] += 1

        r[0] = new_x
        r[1] = new_y

    for row in grid:
        string = "".join(["." if num == 0 else "*" for num in row])
        if "**********" in string:
            search = True
            break
    
    if not search:
        continue

    with open(f"{i+1}.txt", "w") as file:
        for row in grid:
            file.write("".join(["." if num == 0 else "*" for num in row]) + "\n")
