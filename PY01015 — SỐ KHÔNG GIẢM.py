test = int(input())

for _ in range(test): 

    s = input()

    pre = -1 
    check = True 

    for x in s : 
        if int(x) < pre : 
            check = False
            break
        else : pre = int(x)

    print("YES" if check else "NO")

