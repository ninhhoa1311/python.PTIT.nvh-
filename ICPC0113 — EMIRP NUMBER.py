

is_prime = [1]*int(1e6)

is_prime[0] = 0
is_prime[1]=0

for i in range(2,int(1e6)):

    if is_prime[i] == 1:

        j = i * i 

        while j < int(1e6):
            is_prime[j] = 0
            j += i


Prime =[]

for i in range(1,int(1e6)):
    if is_prime[i] == 1:
        Prime.append(i)


def Swap(a):
    s =''
    for x in str(a):
        s = x + s
    return int(s) 


test = int(input())

for _ in range(test):
    num = int(input())

    count = 0 
    index = 0 
    arr = {}

    while Prime[index] < num :

        if Prime[index] in arr :
            index+=1 
        else:
            curr = Swap(Prime[index])
            if curr in arr :
                index +=1 
                continue 
            if is_prime[curr] == 1 and curr < num and curr != Prime[index] :
                print(Prime[index] , curr , end ="")
                arr[Prime[index]]=1
                arr[curr] =1
                print(" ", end ="")
            index+=1

    print()
    