
nums = [int(num) for num in input().strip().split()]

def blink():
    global nums
    new = []
    for num in nums:
        if num == 0:
            new.append(1)
            continue

        temp = num
        length = 0
        while temp:
            temp //= 10
            length += 1


        if length % 2 == 0:
            mod = 10 ** (length // 2)
            new.append(num // mod)
            new.append(num % mod)
        else:
            new.append(num * 2024)

    nums = new

for i in range(25):
    blink()

print(len(nums))