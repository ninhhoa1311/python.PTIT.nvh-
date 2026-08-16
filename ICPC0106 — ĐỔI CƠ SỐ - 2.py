test = int(input())

for i in range(test):

    a =  int(input())
    st = str(input())
    ans = int(st,2)


    tranlate_4 = {

        '00' : '0',
        '01' : '1',
        '10' : '2',
        '11' : '3'
    }

    tranlate_8 = {

        '000' : '0',
        '001' : '1',
        '010' : '2',
        '011' : '3',
        '100'  : '4',
        '101'   : '5',
        '110'   : '6',
        '111'   : '7',
    }

    tranlate_16 ={
        '0000'  : '0',
        '0001'  : '1',
        '0010'  :   '2',
        '0011'  :   '3',
        '0100'  :   '4',
        '0101'  :   '5',
        '0110'  :   '6',
        '0111'  :   '7',
        '1000'  :   '8',
        '1001'  :   '9',
        '1010'  :   'A',
        '1011'  :   'B',
        '1100'  :   'C',
        '1101'  :   'D',
        '1110'  :   'E',
        '1111'  :   'F'
    }




    if a == 2 : 
        print(st)
    elif a == 8 : 

        while len(st) %3 !=0 :
            st ='0' + st
        ans = ''
        for i in range(0,len(st) ,3):
            ans+=tranlate_8[str(st[i : i + 3])]

        print(ans)
    elif a == 16:
        while len(st) % 4 !=0 :
            st ='0' + st
        ans = ''
        for i in range(0,len(st) ,4):
            ans +=tranlate_16[str(st[i : i + 4])]
        print(ans)
      
    elif a == 4: 
        while len(st) % 2 !=0 :
            st ='0' + st
        ans =''
        for i in range(0,len(st) ,2):
            ans+=tranlate_4[str(st[i : i + 2])]

        print(ans)       

        
            
        

