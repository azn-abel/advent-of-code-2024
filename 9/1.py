string = input().strip()

store = []

for i, num in enumerate(string):
    num = int(num)
    if i % 2 != 0:
        store += ["." for _ in range(num)]
    else:
        store += [i // 2 for _ in range(num)]

while "." in store:
    idx = store.index(".")
    last = store[-1]

    if last == ".":
        store.pop()
        continue

    store[idx] = last
    store.pop()

total = 0

for i, val in enumerate(store):
    total += i * val

print(total)
