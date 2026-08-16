
test = int(input())

for _ in range (test): 
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    count = 0 
    for i in range(n - 2): 

        left = i + 1 
        right = n - 1

        while left < right :

            total = arr[i] + arr[left] + arr[right]

            if total == 0 :
                count += 1
                left +=1
                right -=1
            elif total > 0: 
                right-=1
            else : 
                left +=1  
    print(count)