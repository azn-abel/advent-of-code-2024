from collections import deque

SIZE = 140

grid = [list(input().strip()) for _ in range(SIZE)]

visited = set()

res = 0

dirs = ((0,1),(0,-1),(1,0),(-1,0))

def bfs(r, c, l):
    area = 0
    perimeter = 0

    sides = {
        (0, 1): [],
        (0,-1): [],
        (1, 0): [],
        (-1,0): []
    }

    q = deque([(r, c)])

    visited.add((r, c))

    while q:
        i, j = q.popleft()
        area += 1
        for x, y in dirs:
            new_r, new_c = i + x, j + y
            if new_r < 0 or new_r >= SIZE or new_c < 0 or new_c >= SIZE or grid[new_r][new_c] != l:
                perimeter += 1
                if (x, y) in ((1, 0), (-1,0)):
                    sides[(x, y)].append((new_r, new_c))
                else:
                    sides[(x, y)].append((new_c, new_r))
                continue
            if (new_r, new_c) in visited:
                continue
            visited.add((new_r, new_c))
            q.append((new_r, new_c))

    sides[(0,-1)].sort()
    sides[(0, 1)].sort()
    sides[(-1,0)].sort()
    sides[(1, 0)].sort()

    num_sides = 4

    for lst in sides.values():
        for i, val in enumerate(lst):
            if i == 0:
                continue
            prev = lst[i-1]
            if val[0] != prev[0] or abs(val[1] - prev[1]) != 1:
                num_sides += 1
    return area * num_sides

for r in range(SIZE):
    for c in range(SIZE):
        if (r, c) not in visited:
            res += bfs(r, c, grid[r][c])

print(res)