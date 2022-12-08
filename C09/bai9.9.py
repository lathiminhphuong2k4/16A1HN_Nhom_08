#Tính diện tích , chu vi hình tròn với tham số là r(bán kính)
#Tính diện tích , chu vi hình chữ nhật với hàm số là a,b(chiều dài và chiều rộng)
import math
S_hinh_tron=lambda r:math.pi*(r**2)
P_hinh_tron=lambda r:2*r*math.pi
S_hinh_chu_nhat=lambda a,b: a*b
P_hinh_chu_nhat=lambda a,b: (a+b)*2
r=int(input("Nhập bán kính r"))
a=int(input("Nhập chiều dài hình chữ nhật: "))
b=int(input("Nhập chiều rộng hình chữ nhật: "))
print(S_hinh_tron(r),P_hinh_tron(r))
print(S_hinh_chu_nhat(a,b),P_hinh_chu_nhat(a,b))