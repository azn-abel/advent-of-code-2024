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
    
    nodes = set()
    
    for x, y in antennas[curr]:

        if (x, y) == (i, j):
            continue

        diff_x, diff_y = i - x, j - y

        temp_x, temp_y = x, y
        while temp_x >= 0 and temp_y >= 0 and temp_x < 50 and temp_y < 50:
            nodes.add((temp_x, temp_y))
            temp_x += diff_x
            temp_y += diff_y

        temp_x, temp_y = x, y
        while temp_x >= 0 and temp_y >= 0 and temp_x < 50 and temp_y < 50:
            nodes.add((temp_x, temp_y))
            temp_x -= diff_x
            temp_y -= diff_y

    antennas[curr].add((i, j))

    return nodes


for i in range(50):
    for j in range(50):
        for a in get_antinodes(i, j):
            antinodes.add(a)
            with_antinodes[a[0]][a[1]] = "#"

print(len(antinodes))