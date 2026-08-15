is_prime = [1]*1000005

is_prime[0] = 0 
is_prime[1] = 0

for i in range(1, 1000): 

    if is_prime[i] == 1: 
        j = i * i

        while j < int(1e6): 
            is_prime[j] = 0
            j += i

Prime =[]

for i in range(1,int(1e6)): 
    if is_prime[i] == 1: 
        Prime.append(i)


test = int(input())

for _ in range(test): 
    n = int(input())

    cnt = 0 
    count =0


    while Prime[cnt] <= n - 6:

        num = Prime[cnt]

        if is_prime[num] == 1 and (is_prime[num + 2] == 1 or is_prime[num + 4] ==1)and is_prime[num+6] == 1: 
            count+=1 

        cnt +=1 

    print(count)
