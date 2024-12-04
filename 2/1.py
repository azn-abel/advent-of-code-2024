
res = 0

line = None

def is_good(arr):
    ascending = True

    if len(arr) <= 1:
        return True

    if arr[0] > arr[1]:
        ascending = False

    for i, val in enumerate(arr):
        if i == 0:
            continue

        prev = arr[i-1]

        if abs(prev - val) > 3:
            return False

        if prev == val:
            return False

        if prev < val:
            if not ascending:
                return False        
        if prev > val:
            if ascending:
                return False

    return True


while True:
    try:
        line = input().strip()
    except:
        break

    report = [int(num) for num in line.split()]

    if len(report) == 1:
        res += 1 
        continue   

    if is_good(report):
        res += 1

print(res)
