test = int(input())

for _ in range(test):   
    x,y = map(int,(input().split()))

    arr = list(map(int, input().split()))

    arr = arr[y:]+ arr[:y]


    for x in arr: 
        print(x, " " , end ="")

    print("")

