n = input()

count = 0 

for x in n: 
    if x == '7' or x == '4' : 
        count+=1 

print("YES" if count == 4 or count == 7 else "NO")