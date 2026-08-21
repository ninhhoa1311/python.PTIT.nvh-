s = input()

u = 0 
l = 0 

for x in s: 
    if x.isupper() : u+=1 
    else :l+=1 


print(s.upper() if u > l else s.lower())