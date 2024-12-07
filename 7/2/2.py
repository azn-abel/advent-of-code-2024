
def recur(curr, remaining, goal):
    if not remaining:
        if curr == goal:
            return True
        return False
    
    return (
        recur(curr * remaining[0], remaining[1:], goal) or
        recur(curr + remaining[0], remaining[1:], goal) or
        recur(int(str(curr) + str(remaining[0])), remaining[1:], goal)
    )


total = 0

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    chunks = line.split(":")
    goal = int(chunks[0])

    rest = chunks[1].strip()

    nums = [int(num) for num in rest.split()]

    if recur(nums[0], nums[1:], goal):
        total += goal

print(total)
