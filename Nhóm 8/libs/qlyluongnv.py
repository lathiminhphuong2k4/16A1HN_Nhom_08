#Quản lý lương nhân viên
import os ,csv
#Nhóm 08 : DHKL16A1HN
#Lã Thị Minh Phương : 22174600075
#Nguyễn Thị Na : 22174600084
#Nghiêm Anh Tuấn : 22174600076
#Nguyễn Thị Phương Anh :22174600085
import qlyluongnv
lstDanhSach=[]
_path="files/ds_luong_nv.csv"
def mo_file_ds_luong_nhan_vien(_path,lstDanhSach):
    try:
        f=open(_path,'r',encoding='utf-8')
        for dong in csv.reader(f):
            if dong[0]=='so_ds':
                continue
            lstDanhSach.append({'so_ds':dong[0],'so_nv':dong[1],'ho_tennv':dong[2],'luong_ngay':dong[3],'ngay_cong':dong[4],'luong_thang':dong[5],'thuong':dong[6]})
        f.close()
        return 1
    except Exception as ex1:
        print('Không mở được file hợp lệ ',ex1)
        return 0
#--------------hàm lưu danh sách---------------------
def luu_ds_luong_nhan_vien(_path,lstDanhSach):
    try:
        f=open(_path,'w',newline='', encoding = 'utf-8')
        csv.writer(f).writerow(['so_ds','so_nv','ho_tennv','luong_ngay','ngay_cong','luong_thang','thuong'])
        for ds in lstDanhSach:
            csv.writer(f).writerow([ds['so_ds'],ds['so_nv'], ds['ho_tennv'],ds['luong_ngay'],ds['ngay_cong'],ds['luong_thang'],ds['thuong']])
        f.close()
        return 1
    except Exception as ex1:
        return 0
#---------------------------hàm thêm danh sách------------------------
def them_danh_sach(lstDanhSach):
    while True:
        so_ds=input('Nhập số danh sách lương nhân viên: ')
        so_nv=input('Nhập số nhân viên: ')
        ho_tennv=input('Họ tên nhân viên: ')
        luong_ngay=float(input('Lương ngày của nhân viên: '))
        ngay_cong=input('Ngày công của nhân viên: ')
        luong_thang=float(input('Lương tháng của nhân viên: '))
        thuong=float(input('Thưởng: '))
        lstDanhSach.append({'so_ds':so_ds,'so_nv':so_nv,'ho_tennv':ho_tennv,'luong_ngay':luong_ngay,'ngay_cong':ngay_cong,'luong_thang':luong_thang,'thuong':thuong})
        tt=input('Bạn có muốn tiếp tục thêm ? (1:TT)')
        if tt!='1':
            break
        return
#-------------------hàm in danh sách--------------------------------------------------------
def in_ds_luong_nhan_vien(lstDanhSach):
    print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format('so_ds','so_nv','ho_tennv','luong_ngay','ngay_cong','luong_thang','thuong'))
    for ds in lstDanhSach:
        print('{:12}{:12}{:20}{:18}{:20}{:15}{:>20}{:>20}{:>20}'.format(ds['so_ds'],ds['so_nv'],ds['ho_tennv'],ds['luong_ngay'],ds['ngay_cong'],ds['luong_thang'],ds['thuong']))
        return
#----------------Hàm tra cứu danh sách----------------------
def tra_cuu_danh_sach(lstDanhSach,sods):
    for ds in lstDanhSach:
        if ds['so_ds']==sods:
            return ds
    return
#---------------------hàm xóa danh sách-----------------------------
def xoa_danh_sach(lstDanhSach,sods):
    for i in range(len(lstDanhSach)):
        ds=lstDanhSach[i]
        if ds['so_ds']==sods:
            del(lstDanhSach[i])
            return 1
    return 0
#-----------------------Hàm thống kê---------------------
def thong_ke(lstDanhSach):
    tong=0
    tong_thuong=0
    lstDanhSach=[]
    for ds in lstDanhSach:
        tong+=float(ds['tong_tien_luong_nv'])
        tong_thuong+=float(ds['thuong'])
    tong_tien=float(tong+tong_thuong)
    print('Tổng tiền lương tất cả của nhân viên: %f'%tong)
    print('Tổng tiền thưởng của nhân viên: %f'%tong_thuong)
    return
#--------------sắp xếp danh sách------------
def sap_xep(lstDanhSach):
    danh_sach=sorted(lstDanhSach,key=lambda x:x['tong_tien_luong'])
    return danh_sach
#--------------------------BẮT ĐẦU CHƯƠNG TRÌNH QUẢN LÝ----------------------------
print('CHƯƠNG TRÌNH QUẢN LÝ DANH SÁCH LƯƠNG NHÂN VIÊN')
while True:
    print('1:Thêm danh sách lương nhân viên')
    print('2:Danh sách lương nhân viên')
    print('3:Tra cứu danh sách lương nhân viên')
    print('4:Xóa danh sách lương nhân viên ')
    print('5:Thống kê')
    print('6:Lưu danh sách lương nhân viên ra file CSV')
    print('7:Đọc file  CSV')

    chon=int(input('Chọn chức năng cần thực hiện: '))
    if chon ==1:
        them_danh_sach(lstDanhSach)
    elif chon ==2:
        in_ds_luong_nhan_vien(lstDanhSach)
    elif chon ==3:
        sods=input('Nhập số danh sách cần tra cứu')
        ds=tra_cuu_danh_sach(lstDanhSach,sods)
        if ds==None:
            print("Không tra cứu được số danh sách %d"%sods)
        else:
            print(ds)
    elif chon ==4:
        sods=input('Nhập số danh sách cần xóa:')
        kt=input('Bạn có chắc chắn muốn xóa không? (c/C hay k/K?')
        if kt =='c' or kt =='C':
            kq=xoa_danh_sach(lstDanhSach,sods)
            if kq==1:
                print('Đã xóa danh sách',sods)
            else:
                print('Không còn tồn tại danh sách bạn muốn xóa')
    elif chon==5:
        thong_ke(lstDanhSach)
    elif chon==6:
        print('Danh sách trước khi sắp xếp theo tổng tiền là:',in_ds_luong_nhan_vien(lstDanhSach))
        print("Danh sách sau khi sắp xếp theo tổng tiền là:",in_ds_luong_nhan_vien(lstDanhSach))     
    elif chon==7:
        if luu_ds_luong_nhan_vien(_path,lstDanhSach)==1:
            print('Lưu thành công !')
        else:
            print('Không lưu được !!')
        luu_ds_luong_nhan_vien(_path,lstDanhSach)
    elif chon==8:
        if mo_file_ds_luong_nhan_vien(_path,lstDanhSach):
            print("Đã đọc được file vào lstDanhSach")
    else:
        break
    tt=input('Bạn muốn tiếp tục (1:tt)')
    if tt!='1':
        break
    else:
        os.system('cls')
    input('Gõ phím bất kỳ để tiếp tục chương trình !!!')
