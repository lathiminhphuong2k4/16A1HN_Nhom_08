#kiểm tra số hoàn hảo
a=int(input("nhập số "))
b=1
c=0
while b<a:     
     if (a%b==0):
         c=c+b
         print(c)
     b+=1
if c==a:
     print(a,"là số hoàn hảo")
else :
     print(a," không phải là số hoàn hảo")