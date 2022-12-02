#Chương trình tìm min max
a=int(input("Nhập giá trị của a: "))
b=int(input("Nhập giá trị của b: "))
c=int(input("Nhập giá trị của c: "))
d=int(input("Nhập giá trị của d: "))
if a>b>c>d:
    print("a là giá trị lớn nhất")
elif b>c>d>a:
    print("b là giá trị lớn nhất")
elif c>b>a>d:
    print("c là giá trị lớn nhất")
elif d>c>b>a:
    print("d là giá trị lớn nhất")