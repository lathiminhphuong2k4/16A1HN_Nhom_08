#chương trình kiểm tra năm nhuận
x=int(input("nhập năm: "))
if x%4==0 :
    print("năm",x, "là năm nhuận")
elif x%100 !=0:
    print("năm",x, "là năm nhuận")
elif x%400 == 0:
    print("năm",x, "là năm nhuận")
else:
    print("năm",x, "là năm không nhuận")