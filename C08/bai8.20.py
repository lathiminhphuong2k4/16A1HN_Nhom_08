#chương trình tính gần đúng giá trị hàm e^x với sai số 10^-4
import math
x=float(int(input("Nhập vào giá trị của x = ")))
Ex=1
n=1
t=x
while math.fabs(t)>=0.0001: #(10 mũ -4)
    Ex+=t
    n+=1
    # t*=x/(float(n))
    t=t*(x/(float(n)))
print("Giá trị gần đúng của e mũ x là %0.6f"%Ex)