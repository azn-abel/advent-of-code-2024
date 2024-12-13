import numpy as np

res = 0

for i in range(320):
    a = tuple(int(seq[2:]) for seq in input().strip().split(": ")[1].split(", "))
    b = tuple(int(seq[2:]) for seq in input().strip().split(": ")[1].split(", "))
    prize = tuple(int(seq[2:]) for seq in input().strip().split(": ")[1].split(", "))

    prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)

    A = np.array([[a[0], b[0]], [a[1], b[1]]])
    B = np.array(prize)

    As, Bs = np.linalg.solve(A, B)

    if abs(As - round(As)) < 0.00005 and abs(Bs - round(Bs)) < 0.00005:
        res += 3 * round(As) + round(Bs)

    try:
        input()
    except EOFError:
        continue

print(res)
