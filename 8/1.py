grid = [list(input().strip()) for _ in range(50)]

with_antinodes = [row.copy() for row in grid]

antennas = {}

antinodes = set()

def get_antinodes(i, j):
    curr = grid[i][j]
    if not curr.isalnum():
        return []

    if not curr in antennas:
        antennas[curr] = {(i, j)}
        return []
    
    rtn = []
    
    for x, y in antennas[curr]:

        if (x, y) == (i, j):
            continue

        diff_x, diff_y = i - x, j - y
        a1 = (i + diff_x, j + diff_y)
        a2 = (x - diff_x, y - diff_y)

        if not (a1[0] < 0 or a1[1] < 0 or a1[0] >= 50 or a1[1] >= 50):
            rtn.append(a1)
        if not (a2[0] < 0 or a2[1] < 0 or a2[0] >= 50 or a2[1] >= 50):
            rtn.append(a2)

    antennas[curr].add((i, j))

    return rtn



for i in range(50):
    for j in range(50):
        for a in get_antinodes(i, j):
            antinodes.add(a)
            with_antinodes[a[0]][a[1]] = "#"

print(len(antinodes))