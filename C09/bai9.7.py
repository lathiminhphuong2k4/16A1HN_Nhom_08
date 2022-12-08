#Viết hàm trả về phần nguyên của phép chia hai số nguyên  
def chia_nguyen(x1,x2):
    chia_nguyen=x1//x2
    return chia_nguyen
x1=int(input("Nhập x1: "))
x2=int(input("Nhập x2: "))
print("Phần nguyên là: ",chia_nguyen(x1,x2))