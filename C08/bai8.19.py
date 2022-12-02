#Xây dựng chương trình đảo ngược một dãy số với số lượng tùy ý bắt đầu
#ví dụ
#Nhập vào:1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#In ra:19 17 15 13 11 9 7 5 3 1
n=int(input("Nhập số n= "))
i=int(1)
day_so = ""
print("Nhập dãy số , bắt đầu = số 1 :")
while i<n:
    i=int(input("1= "))
    day_so += str(1)
#Sử dụng chuỗi kết quả để đảo ngược dãy số nhập ở trên
kq=""
for ch in day_so:
    kq=ch+kq
#In ra các số lẻ theo thứ tự đảo ngược của dãy số
for ch in kq:
    if int(ch)%2 !=0:
        print(ch, end  ="")