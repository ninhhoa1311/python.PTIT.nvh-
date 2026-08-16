
count = int(input())

for i in range(count): 
    s = input()

    arr = ['0','1','2','3','4','5','6','7','8','9']

    Min = 0
    a = ''
    for x in s: 
        if x in arr:
            a += x 
        elif len(a) > 0 and len(a) <= 18:
            Min = max(int(a),Min)
            a = ''


    if len(a) > 0 : 
        Min = max(int(a) , Min)

    print(Min)