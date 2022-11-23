#Cho giá trị var = 10; in ra màn hình các số chẵn lớn hơn 5 và <=10. ,
# sau đó in ra màn hình thông báo "Kết thúc lặp !"
var = 10 
while var >0:
    if var % 2 == 0:
        print("Giá trị :",var)
    var -=1
    if var ==5:
        break
print("Kết thúc vòng lặp !")
