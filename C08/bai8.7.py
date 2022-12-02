#chương trình để tính tiền điện
x=int(input("nhập số kwh"))
if x<=50:
    print("tiền điện phải trả là: ",x*1.678 )
elif x<=100:
       print("tiền điện phải trả là: ", (x-50)*1.734 +50*1.678)
elif x<=200:
    print("tiền điện phải trả là: ",50*1.678 + 100*1.734 +(x-100)*2.014 )
elif x<=300:
    print("tiền điện phải trả là: ",50*1.678 + 100*1.734+ 200*2.014 + (x-200)*2.536)
elif x<=400:
       print("tiền điện phải trả là: ",50*1.678 + 100*1.734+ 200*2.014 +300*2.536 + (x-300*2.824 ))
else:
    print("tiền điện phải trả là: ",50*1.678 + 100*1.734+ 200*2.014 +300*2.536 + 400*2.834 + (x-400)*2.927)