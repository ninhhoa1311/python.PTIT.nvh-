test = int(input())

for _ in range(test): 
    s = input()

    pre = ''
    for x in s : 
        if x.isalpha(): pre = x 
        else : 
            for _ in range(int(x)): 
                print(pre , end = "")

    print("")