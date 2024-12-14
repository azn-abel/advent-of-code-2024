COLS = 101
ROWS = 103

INPUT_SIZE = 500

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

for _ in range(INPUT_SIZE):
    pv = input().strip().split()
    p = tuple(int(x) for x in pv[0][2:].split(","))
    v = tuple(int(x) for x in pv[1][2:].split(","))

    res = ((p[0] + 100 * v[0]) % COLS, (p[1] + 100 * v[1]) % ROWS)

    grid[res[1]][res[0]] += 1

q1 = 0
q2 = 0
q3 = 0
q4 = 0

border_i = ROWS // 2
border_j = COLS // 2

print(border_i, border_j)

for row in grid:
    print(row)

for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if i < border_i and j < border_j:
            q1 += val
        elif i < border_i and j > border_j:
            q2 += val
        elif i > border_i and j < border_j:
            q3 += val
        elif i > border_i and j > border_j:
            q4 += val

print(q1, q2, q3, q4)
print(q1 * q2 * q3 * q4)