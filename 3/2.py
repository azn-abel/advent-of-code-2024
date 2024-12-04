line = input().strip()

length = len(line)

total = 0

do = True

for start in range(0, length - 8):
    
    if line[start:start+4] == "do()":
        do = True
        continue

    if line[start:start+7] == "don't()":
        do = False
        continue

    if not do:
        continue
    
    if line[start:start+4] != "mul(":
        continue

    num_start = start+4
    num_end = None

    for end in range(num_start, num_start + 8):
        if line[end] == ")":
            num_end = end
            break
    else:
        continue

    num_line = line[num_start:num_end]
    try:
        factors = [int(num) for num in num_line.split(",")]
    except:
        continue

    if len(factors) != 2:
        continue

    total += factors[0] * factors[1]


print(total)
