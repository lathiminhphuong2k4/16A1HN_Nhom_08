#tính năm âm lịch
nam_duong_lich=int(input("nhập năm: "))
def tinh_can(nam):
    nam=int(nam%10)
    if nam==0:
        print("Canh")
    elif nam==1:
        print("Tân")
    elif nam==2:
        print("Nhâm")
    elif nam==3:
        print("Quý")
    elif nam==4:
        print("Giáp")
    elif nam==5:
        print("Ất")
    elif nam==6:
        print("Bính")
    elif nam==7:
        print("Đinh")
    elif nam==8:
        print("Mậu")
    else :
        print("Kỷ")
    return
def tinh_chi(nam):
    nam=int(nam%12)
    if nam==0:
        print("Thân")
    elif nam==1:
        print("Dậu")
    elif nam==2:
        print("Tuất")
    elif nam==3:
        print("Hợi")
    elif nam==4:
        print("Tý")
    elif nam==5:
        print("Sửu")
    elif nam==6:
        print("Dần")
    elif nam==7:
        print("Mão")
    elif nam==8:
        print("Thìn")
    elif nam==9:
        print("Tỵ")
    elif nam==10:
        print("Ngọ")
    else :
        print("Mùi")
    return