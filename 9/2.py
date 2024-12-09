string = input().strip()

store = []

for i, num in enumerate(string):
    num = int(num)
    if i % 2 != 0:
        store += ["." for _ in range(num)]
    else:
        store += [i // 2 for _ in range(num)]

curr = i // 2

while curr >= 0:

    count_curr = store.count(curr)

    idx = store.index(".")
    end = store.index(curr)

    count_empty = 0
    start_idx = idx

    shifted = False

    while idx <= end:

        if store[idx] == ".":
            count_empty += 1

        else:
            if count_curr <= count_empty:
                for i in range(count_curr):
                    store[start_idx + i] = curr
                    store[end + i] = "."
                shifted = True
                break
            count_empty = 0
            start_idx = idx + 1

        idx += 1

    curr -= 1

total = 0

for i, val in enumerate(store):
    if isinstance(val, int):
        total += i * val

print(total)
