#xây dựng phương thức tính S(n,x)
import math
def tinh_S(n,x):
    S=math.pow(math.pow(x,2)+1,n)
    return S
n=int(input("Nhập n: "))
x=int(input("Nhập x: "))
print("S =",tinh_S(n,x))