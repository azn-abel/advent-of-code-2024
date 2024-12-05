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
        for j, prev in enumerate(arr[:i]):
            if val in cache[prev]:
                arr[i], arr[j] = arr[j], arr[i]
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
        continue

    while not is_good(nums):
        is_good(nums)

    res += nums[len(nums) // 2]

print(res)
