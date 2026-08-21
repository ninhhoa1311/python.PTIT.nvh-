import math 


def check_snt(n):
    if n <= 1: return False 
    if n == 2: return True 
    if n % 2 == 0 : return False 

    for i in range(3 , int(math.sqrt(n)) + 1, 2): 
        if n % i == 0 : return False 

    return True 

test = int(input())

for _ in range(test):
    a,b = map(int,input().split())

    c = math.gcd(a,b)

    sum = 0 
    while c > 0 : 
        sum += c%10 
        c//=10 

    print("YES" if check_snt(sum) else "NO")