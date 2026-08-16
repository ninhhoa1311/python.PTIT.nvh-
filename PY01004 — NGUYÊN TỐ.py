import math

test = int(input())

def check(a): 
    if a <= 1 : return False 

    for i in range(2,int(math.sqrt(a)) + 1): 
        if a % i == 0: 
            return False 

    return True 


for _ in range(test): 
    n = int(input())

    count = 0 

    for i in range(1, n): 
        if math.gcd(i,n) == 1: 
            count+=1

    print("YES" if check(count) else "NO")