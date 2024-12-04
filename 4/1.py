
count = 0

grid = []

dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def search(r, c, d):
    global count
    cand = "X"

    new_r = r
    new_c = c

    for _ in range(3):
        new_r += d[0]
        new_c += d[1]
        if new_r < 0 or new_c < 0:
            return
        if new_r > 139 or new_c > 139:
            return
        cand += grid[new_r][new_c]

    if cand == "XMAS":
        count += 1


for _ in range(140):
    grid.append(list(input().strip()))

for i in range(140):
    for j in range(140):
        if grid[i][j] == "X":
            for d in dirs:
                search(i, j, d)

print(count)

