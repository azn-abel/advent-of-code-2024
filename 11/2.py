
from collections import Counter

nums = [int(num) for num in input().strip().split()]

mapping = {
    0: [1]
}

counter = Counter(nums)

def blink():
    global counter
    new = {}
    for num in counter:
        count = counter[num]
        if num in mapping:
            for n in mapping[num]:
                if n not in new:
                    new[n] = 0
                new[n] += count
            continue

        temp = num
        length = 0
        while temp:
            temp //= 10
            length += 1

        if length % 2 == 0:
            mod = 10 ** (length // 2)
            first = num // mod
            second = num % mod
            if first not in new:
                new[first] = 0
            if second not in new:
                new[second] = 0
            new[first] += count
            new[second] += count
            mapping[num] = [first, second]
        else:
            prod = num * 2024
            if prod not in new:
                new[prod] = 0
            new[prod] += count 
            mapping[num] = [prod]

    counter = new

for i in range(75):
    blink()

print(sum(counter.values()))