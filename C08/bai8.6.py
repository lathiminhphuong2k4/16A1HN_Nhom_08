#tính cước xe tacxi
a=int(input("chọn xe có 4 hay 7 chỗ "))
b=int(input("nhập số km "))
c=int(input("nhập thời gian chờ "))
if c<=5:
    c=0
if a==4 :
    if b<=0.8 :
        b= 11000
    if (b<=20)and(b>=0.8):
        b=b*12100
    else:
        b= (b-20)*10000 + 242000
    if c>5:
        c=(c-5)*800
    print("số tiền phải trả",b+c)
if a==7 :
    if b<=0.8 :
        b= 13000
    if (b<=20)and(b>=0.8):
        b= b*14100
    else:
        b= (b-20)*12000 + 282000
    if c>5:
        c=(c-5)*800
    print("số tiền phải trả",b+c)
if (a!=4)and(a!=7):
    print("không có xe")