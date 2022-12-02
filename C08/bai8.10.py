#Nhập vào một số nguyên n và một số thực x. 
# Tính và in ra kết quả sau: 
#   S = (x2 + 1)^n
n = int(input("Nhập vào số nguyên n = "))
x= float(input("NHập vào số thực x = "))
S=1
i=int(0)
bt = x*x+1
while i<n:
    S*=bt
    i+=1
print("S = %0.2f"%S)