#Nhập vào một số nguyên n và một số thực x.
#Tính và in ra kết quả sau:
#   S = (x2 + 1)^n
import math
n = int(input("Nhập vào số nguyên n = "))
x= float(input("Nhập vào số thực x = "))
S=0
i=int(0)
S= [(x*x+1)]
while i<n:
    S=math.pow(S,i-1)          #i=1 --> S=S*S; i=2 --> S=S*S*S
    i+=1
print("S = %0.2f"%S)