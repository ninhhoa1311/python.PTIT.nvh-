def sum (x, a, b):
    ans = str(x).replace(str(a),str(b))
    return int(ans)



test = int(input())

for _ in range(test):

    a,b = map(int,input().split())

    
    x = input().strip()
    if(x.count(" ")) : x,y = x.split()
    else : y = int(input())
    
    if  a > b : 
        a,b = b,a 

    max_int = sum(x,a,b) + sum(y,a,b)
    min_int = sum(x,b,a) + sum(y,b,a)

    print(f"{min_int} {max_int}"); 
