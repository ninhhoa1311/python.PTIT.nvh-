test = int(input())

for _ in range(test):

    s = list(map(int,input()))

    if len(s) == 1: 
        print(s[0])
        continue

    n = len(s) - 1

    Carry =  False 

    while n > 0 : 

        if Carry : 
            s[n]+=1
            Carry = False 

        if s[n] >=5 : 
            Carry = True 

        s[n] = 0
        n-=1 

    if Carry : s[0] += 1

    for x in s: 
        print(x, end ="")
    print("")
    
                   
