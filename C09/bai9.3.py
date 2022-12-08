#Viết chương trình tính chỉ số BMI
import math
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/math.pow(chieu_cao,2)
    if bmi < 18.5:
        print("Bạn Gầy!!!")
    elif (bmi >= 18.5) and (bmi <= 22.99) :
        print("Bạn bình thường !")
    elif bmi >= 25:
        print("Bạn đã thừa cân !!!!!!!")
    return bmi

can_nang=int(input("Nhập cân nặng của bạn: "))
chieu_cao=float(input("Nhập chiều cao của bạn: "))
print("chỉ số BMI của bạn là: ",tinh_bmi(can_nang,chieu_cao))