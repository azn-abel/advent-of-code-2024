
arr1 = []
arr2 = []

ans = 0

while True:
    try:
        line = input()
    except:
        break

    x1, x2 = [int(num) for num in line.strip().split()]

    arr1.append(x1)
    arr2.append(x2)
   
arr1.sort()
arr2.sort()

for i, val in enumerate(arr1):
    other = arr2[i]
    ans += abs(other - val)

print(ans)
