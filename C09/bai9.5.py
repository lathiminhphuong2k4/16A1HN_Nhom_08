#xây dựng phương thức tính A(n,x)
import math
def tinh_A(n,x):
    A=math.pow(math.pow(x,2)+x+1,n)+math.pow(math.pow(x,2)-x+1,n)
    return A
n=int(input("Nhập n: "))
x=int(input("Nhập x: "))
print("A =",tinh_A(n,x))