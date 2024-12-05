cache = {}

for _ in range(1176):
    needs, page = [int(num) for num in input().strip().split("|")]
    if page in cache:
        cache[page].add(needs)
    else:
        cache[page] = {needs}

input()

def is_good(arr):
    for i, val in enumerate(arr):
        for prev in arr[:i]:
            if val in cache[prev]:
                return False
            
    return True


res = 0

while True:
    try:
        line = input()
    except EOFError:
        break

    nums = [int(num) for num in line.strip().split(",")]
    if is_good(nums):
        res += nums[len(nums) // 2]

print(res)
