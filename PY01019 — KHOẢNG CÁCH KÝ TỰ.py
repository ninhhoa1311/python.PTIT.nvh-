test = int(input())

for _ in range(test): 

    s = input()

    n = len(s)
    i = 1
    check = True 
    while i <= n - i -1 : 
        sub1 = abs(ord(s[i]) - ord(s[i-1]))
        sub2 = abs(ord(s[n-i-1]) - ord(s[n-i]))

        if sub1 != sub2 : 
            check = False 
            break

        i += 1 

    print("YES" if check else "NO")
         