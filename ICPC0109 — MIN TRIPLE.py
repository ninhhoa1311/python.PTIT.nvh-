test = int(input())

for _ in range(test): 
    n = int(input())
    arr = list(map(int,input().split()))
    
    min1 = min2 = min3 = -10^8
    for x in arr: 

        if x > min1 : 
            min3 = min2 
            min2 = min1 
            min1 = x 
            
        elif  x > min2 and x < min1 : 
            min3 = min2 
            min2 = x
        elif  x > min3: 
            min3 = x 


    print(min1 + min2 + min3)

