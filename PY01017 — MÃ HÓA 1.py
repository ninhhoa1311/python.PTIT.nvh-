test = int(input())

for _ in range(test): 

    s = input()

    pre = s[0]
    sum = 1 

    for i in range(1, len(s)): 
        x = s[i]
        if x == pre: 
            sum+=1 
        elif x != pre : 
            print(sum,pre,sep = "" , end = '' )
            pre = x 
            sum = 1 

    print(sum, pre , sep = "" , end = "")
    print()
    
    
           
