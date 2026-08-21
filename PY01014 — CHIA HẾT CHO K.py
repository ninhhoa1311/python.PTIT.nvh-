a,k,n = map(int,input().split())

b = (a//k + 1)*k - a 

if a + b > n: print(-1)
else : 
     
    while a + b <= n: 
        print(b , " " , end ='')
        b += k 
        

    