#tính tiền thuê phòng của resot
import fractions
print("có các loại phòng: ")
print("1. Standard")
print("2. Superior Garden View")
print("3. Superior Ocean View")
print("4. Garden View Bungalow")
print("5. Pool View Bungalow")
print("6. Family Room")
print("7. Beach Front Bungalow")
print("8. VIP sea View")
loai_phong=int(input("nhập loại phòng: "))
so_dem_o=int(input("nhập số đêm ở: "))
if so_dem_o==1:
    if loai_phong==1:
        print("số tiền: ",1260000)
    elif loai_phong==2:
        print("số tiền: ",1550000)
    elif loai_phong==3:
        print("số tiền: ",1830000)
    elif loai_phong==4:
        print("số tiền: ",1830000)
    elif loai_phong==5:
        print("số tiền: ",2120000)
    elif loai_phong==6:
        print("số tiền: ",2120000)
    elif loai_phong==7:
        print("số tiền: ",2540000)
    elif loai_phong==8:
        print("số tiền: ",4800000)
elif so_dem_o==2:
    if loai_phong==1:
        print("số tiền: ", 1260000+1260000*25/100)
    elif loai_phong==2:
        print("số tiền: ", 1550000+1550000*25/100)
    elif loai_phong==3:
        print("số tiền: ", 1830000+1830000*25/100)
    elif loai_phong==4:
        print("số tiền: ", 1830000+1830000*25/100)
    elif loai_phong==5:
        print("số tiền: ", 2120000+2120000*25/100)
    elif loai_phong==6:
        print("số tiền: ", 2120000+2120000*25/100)
    elif loai_phong==7:
        print("số tiền: ", 2540000+2540000*25/100)
    elif loai_phong==8:
        print("số tiền: ", 4800000+4800000*25/100)
elif so_dem_o>=4:
    if loai_phong==1:
        print("số tiền: ", 1260000+1260000*30/100)
    elif loai_phong==2:
        print("số tiền: ", 1550000+1550000*30/100)
    elif loai_phong==3:
        print("số tiền: ", 1830000+1830000*30/100)
    elif loai_phong==4:
        print("số tiền: ", 1830000+1830000*30/100)
    elif loai_phong==5:
        print("số tiền: ", 2120000+2120000*30/100)
    elif loai_phong==6:
        print("số tiền: ", 2120000+2120000*30/100)
    elif loai_phong==7:
        print("số tiền: ", 2540000+2540000*30/100)
    elif loai_phong==8:
        print("số tiền: ", 4800000+4800000*30/100)