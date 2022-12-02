#kiểm tra số nguyên tố
a= int(input("nhập số "))
b = 2
if (a == 1 ) :
    print("không phải là số nguyên tố")
while (a>=b):
         if(a==b):
                  print(a,"là số nguyên tố")
                  break
         if (a%b==0):
                  print(a,"không phải là số nguyên tố")
                  break    
         b+=1