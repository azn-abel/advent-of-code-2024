
grid = [[int(num) for num in list(input().strip())] for _ in range(8)]

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def recur(i, j):

    curr = grid[i][j]

    if curr == 9:
        return 1
    
    total = 0

    for x, y in dirs:
        i2, j2 = i + x, j + y

        if i2 < 0 or i2 >= 8:
            continue
        if j2 < 0 or j2 >= 8:
            continue
        if grid[i2][j2] != curr + 1:
            continue

        total += recur(i2, j2)

    return total


ans = 0

for i in range(8):
    for j in range(8):
        if grid[i][j] == 0:
            ans += recur(i, j)

print(ans)