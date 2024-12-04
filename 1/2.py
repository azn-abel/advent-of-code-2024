
arr1 = []

ans = 0

similarity = {}

while True:
    try:
        line = input()
    except:
        break

    x1, x2 = [int(num) for num in line.strip().split()]

    arr1.append(x1)

    if x2 in similarity:
        similarity[x2] += 1 
    else:
        similarity[x2] = 1

for val in arr1:
    if val not in similarity:
        continue
    
    ans += similarity[val] * val

print(ans)
