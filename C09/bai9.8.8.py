#Viết hàm kiểm tra một số có phải số hoàn hảo
x=int(input("Nhập một số: "))
tong=0
for i in range(1,x-1):
    if x%i==0:
        tong+=1
if tong==x:
    print("số",x,"là số hoàn hảo")
else:
    print("số",x,"không phải số hoàn hảo")