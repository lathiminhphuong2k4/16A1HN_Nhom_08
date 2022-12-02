#Nhập vào một số nguyên n và một số thực x. Tính và in ra kết quả của biểu thức sau:
#  A = (x2 + x + 1)^n + (x2 - x + 1)^n
n=int(input("Nhập số nguyên n = "))
x=float(input("NHập số thực x = "))
P=int(1)
Q=int(1)
i=int(0)
bt1=x*x+x+1
bt2=x*x-x+1
while i<n:
    P*=bt1
    Q*=bt2
    i+=1
A=float(P+Q)
print("A = %0.2f"%A)