test = int(input())

for _ in range(test):
    n = input()

    check = True

    for x in n: 
        if x != '7' and x != '4' : 
            check = False  

    print("YES" if check else "NO")