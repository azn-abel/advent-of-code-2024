
grid = [[int(num) for num in list(input().strip())] for _ in range(45)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

cache = set()

def recur(i, j):

    curr = grid[i][j]


    if curr == 9:
        cache.add((i, j))
        return
    

    for x, y in dirs:
        i2, j2 = i + x, j + y

        if i2 < 0 or i2 >= 45:
            continue
        if j2 < 0 or j2 >= 45:
            continue
        if grid[i2][j2] != curr + 1:
            continue

        recur(i2, j2)


ans = 0

for i in range(45):
    for j in range(45):
        if grid[i][j] == 0:
            cache = set()
            recur(i, j)
            ans += len(cache)

print(ans)