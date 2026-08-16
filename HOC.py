#  print(object , sep = seperator , end = end)

'''  day la chu thich tren nhieu dong    '''


# print(type(a)); 
    
'''   khong dc in cu phap co dau cach
      khong dc cbat dau bang chu so 
      khong dc chua ki tu dac biet 

 '''


# kieu du lieu 

'''
    in ra theo hệ số

    - nhị phân 
        0b hoặc 0B --- VD : a = 0b1101
                            print(a) 
    - bát phân 
        0o hoặc 0O ----- VD a = 0o123
                            print(a); 

    - Hệ 16 
        0X hoặc 0x-------VD a= 0x22A
                        print(a)
'''



# in số thực với số lượng sau dấu phẩy xác định 

'''

a = 28.04112323

- print('%.2f' % a)
- print(round(a,2))
- print('{:.2f}'.format(a))


'''


# in số phức 

'''
    a = 3 + 5j 
    in thực :  print(a.real)
    in ảo   :  print(a.imag)

'''

# kiểu dữ liệu đúng sai 

'''
     a = True
     0 và sâu rỗng thì sẽ in ra là false

'''


# string

''' 
    
    in ra trong 1 dòng
    s = 'ninh van hoa' 
    
    in ra co ca xuống dòng bằng 3 dấu phẩy động ''' '''


'''

# ép kiểu 

'''
    s = '12334455' 
    a = int(s)

'''


# toán tử

''' 

gán a,b = b,a 


lũy thứa là                 ** 
chia lấy phần thập phân :   /
chia lấy số nguyên          //
chia dư                     % 


so sáng 

== 
>= 
<=
!= 


điều kiện 

print((x > 20) and (x < 100) )
                or
                not


- is//is not để xác định xem phần tử đó có cùng địa chỉ và giá trị với toán tử cần xét không 

- in xác định xem phần tử đó có nằm trong chuỗi ko 


'''

# nhập vào từ bàn phím

'''

    cú pháp 

    input(prompt)


    lưu ý hàm trả về str phải ép kiểu như mong muốn 

'''

# tách chuỗi số sau khi nhập

'''
    s= input(); 
    a = s.split()

    cú pháp ngắn gọn 

    x, y, z, t = map(int , input().split())
'''

# hàm phổ biến 

'''
    -cách truy cập 
        import math
        from math import * 


    - căn bậc 2 (float)  
        math.sprt(số hạng)

    - căn bậc 2 (integer)
        math.isqrt(số hạng)

    - mũ 2 
        pow( tt1 , tt2 )

    - hàm làm tròn lên 
        cell( tt )
    
    - hàm làm tròn xuống 
        floor(tt)
    
    - hàm làm tròn lên và xuống 
        round ( tt )

    - hàm tính giai thừa 
        factorial( tt )

    - hàm tính ước chung lớn nhất 
        gcd (tt1 , tt2)

    - hàm tính tổ hợp chập k của n 
        comb ( n , k )

    - Hoán vị
        perm ( n )
    
    - trị tuyệt đối 
        fabs ( n )

'''



# cấu trúc rẽ nhánh 

"""
    - cú pháp 
        if condition : 
            #code
        else :

    - cú pháp 

        if condition :
            #code 
        elif condition2 :
            #code 
        else : 
        
    - toán tử 3 ngôi 

        varibale = statement if condition else statement 

        vd: a , b = 100 , 200 
            res = 'ninh van hoa' if a < b else 'ninh ninh' 
            print(res)

"""

# vòng lặp 

'''
    - vòng lặp for 
        hàm range()
    - cú pháp 
        for var in iterable 

    - cú pháp hàm range() dùng để sinh ra 1 dãy số để vòng for duyệt qua từng số trong dãy số đã sinh ra 
        range ( start , stop , step)


    - continue , break 
    
    - vòng lặp while   
        - cú pháp 
            while condition : 
                #code when condition is true
            else : 
                #code while condition is False
'''


# list 

"""
    List are odered : các phần tử trong list là có thứ tự 
    Accessed by index : Truy cập các phần tử trong list thông qua chỉ số
    List can contain any sort of object: list có thể chứa mọi object thuộc kiểu dữ liệu khác nhau 
    Lists are changeable : các phần tử trong list có thể thay đổi giá trị các thao tác thêm xóa phần tử cũng được hỗ trợ 
    

    chỉ số bắt đầu từ 0 

    - list()
        biển đổi 1 đối tượng thành list 
    
    - len()
        biết số lượng phần tử trong list 

    - tạo list 
        a = []
        a = list(chuỗi cần tạo list)

    - cách thay đổi phần tử trong list 

        a = [0 , 1 , 2 , 3 , 4]
            - 5 , - 4 , , -3 , -2 , - 1

        khi thao tác có thể sử dụng index âm để thay đổi 

        vd a[0] = 10
            a[-5] = 10 

    - append() (hàm thêm phần tử vào cuối trong list)
        vd : a.append(100)

    - insert(vị trí , object thêm)  (hàm thêm phần tử vào 1 vị trí bất kì)

        vd : a.insert(2, 100)

    - pop()

        hàm pop() sẽ xóa phần tử cuối vd: a.pop()
        hàm pop() sẽ xóa phần tử thao tác bằng index  vd : a.pop(2)

    - remove()
        hàm xóa phần tử thông quá giá trị của phần tử đó chỉ xóa 1 cái nếu có nhiều phần tử đó trong list
        vd : a.remove(2)

    - sao chép list

        a = [1,2,3]
        b = a*2
        print(b)
    
    - tìm kiếm phần tử trong list 
        if pt in a : 
        
    - thêm phần tử từ list này vào list khác 
        dùng dấu + hoặc extend

        VD : a+= b
            a.extend(b)

    - tạo bản sao 
        c= a.copy()

    - index()
        trả về chỉ số đầu tiên của 1 phần tử trong list

    - reveser()
        lật ngược list 
    
    - sort()
        sắp xếp phần tử trong list 
"""

# ki thuat list clicing

'''
    - kĩ thuật giúp cắt các phần tử trong list 

''' 

# Stack

'''
    - hàm gọi lại chính nó là hàm đệ quy 

'''

# Hàm trong python 

'''
    - Cú pháp 
        def name (argument) :
            statement 
            .....
            return value 


    Note : khi xây dựng code cần sử dùng hàm thì phải có hàm main

    - cú pháp 
        if __name__ == '__main__'


'''
# cách chuyển từ hệ số này sang hệ số khác
"""
int ("giá trị",cơ số )

"""
# cach tac cac so khoi chuoi gom nhieu ki tu 
'''
    import re 
    arr = re.split(r"\D+",s)

    
'''