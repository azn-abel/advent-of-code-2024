
count = 0

grid = []

dirs = [(1,1),(1,-1),(-1,1),(-1,-1)]

cache = set()

def search(r, c, d):
    global count
    cand = "M"

    new_r = r
    new_c = c

    for _ in range(2):
        new_r += d[0]
        new_c += d[1]

        if new_r < 0 or new_c < 0:
            return
        if new_r > 139 or new_c > 139:
            return
        cand += grid[new_r][new_c]

    if cand != "MAS":
        return
    
    mas = [(r,c), (new_r, new_c)]
    mas = tuple(sorted(mas))

    complement = [(mas[1][0], mas[0][1]), (mas[0][0], mas[1][1])]
    complement = tuple(sorted(complement))

    if complement in cache:
        count += 1

    cache.add(mas)


for _ in range(140):
    grid.append(list(input().strip()))

for i in range(140):
    for j in range(140):
        if grid[i][j] == "M":
            for d in dirs:
                search(i, j, d)

print(count)

