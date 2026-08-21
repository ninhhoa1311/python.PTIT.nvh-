test = int(input())

for _ in range(test): 

    n,x,m = map(float,input().split())

    year = 0
    a = n 
    while n < m:
        n = a 
        n = n*((1+(x/100))**year)
        year+=1 

    print(year-1)
