
def recur(curr, remaining, options):
    if not remaining:
        options.append(curr)
        return
    
    recur(curr * remaining[0], remaining[1:], options)
    recur(curr + remaining[0], remaining[1:], options)


def compute(nums):
    options = []

    recur(nums[0], nums[1:], options)

    return options


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

    if goal in compute(nums):
        total += goal

print(total)
