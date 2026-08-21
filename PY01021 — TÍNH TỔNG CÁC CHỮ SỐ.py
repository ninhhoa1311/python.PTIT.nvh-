test = int(input())

for _ in range(test): 
    s = list(input())
    sum = 0 
    result = []

    for x in s: 
        if x.isdigit(): 
            sum += int(x)
        else : 
            result.append(x)

    result.sort()

    for x in result: 
        print(x, end = "")
    print(sum)