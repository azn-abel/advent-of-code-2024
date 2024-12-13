
cache = {}

def solve(a, b, prize, curr, tokens):
    if curr[0] == prize[0] and curr[1] == prize[1]:
        cache[(a, b, curr, tokens)] = tokens
        return tokens
    if curr[0] > prize[0] or curr[1] > prize[1]:
        cache[(a, b, curr, tokens)] = float("inf")
        return float("inf")
    
    if (a, b, curr, tokens) in cache:
        return cache[(a, b, curr, tokens)]
    
    using_a = solve(a, b, prize, (curr[0] + a[0], curr[1] + a[1]), tokens + 3)
    using_b = solve(a, b, prize, (curr[0] + b[0], curr[1] + b[1]), tokens + 1)

    cache[(a, b, curr, tokens)] = min(using_a, using_b)

    return min(using_a, using_b)

res = 0

for i in range(320):
    cache = {}
    a = tuple(int(seq[2:]) for seq in input().strip().split(": ")[1].split(", "))
    b = tuple(int(seq[2:]) for seq in input().strip().split(": ")[1].split(", "))
    prize = tuple(int(seq[2:]) for seq in input().strip().split(": ")[1].split(", "))
    
    temp = solve(a, b, prize, (0, 0), 0)
    if temp != float("inf"):
        res += temp

    try:
        input()
    except EOFError:
        continue

print(res)