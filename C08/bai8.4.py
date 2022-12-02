#Tính diện  tích tam giác
import math
a = int(input("Nhập độ dài cạnh a  "))
b = int(input("Nhập độ dài cạnh b  "))
c = int(input("Nhập độ dài cạnh c  "))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-c)*(p-b))
print("diện tích tam giác là",S)