#tính diện tích tam giác biết số đo 3 cạnh a, b, c theo công thức Hero
import math     #import thư viện toán học để sử dụng hàm tính căn 2,sqrt
print("Nhập số đo 3 cạnh của tam giác ABC")
a = eval(input(' số đo cạnh a = '))
b = eval(input(' số đo cạnh b = '))
c = eval(input(' số đo cạnh c = '))
p = (a+b+c)/2    #công thức tính nửa chu vi
S = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác ABC đã cho là: ", S)
