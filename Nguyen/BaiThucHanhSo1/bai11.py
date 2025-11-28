import math

x = float(input('nhap x '))
if x > 0:
    C = math.log(x) + math.exp(x) + math.sqrt(abs(x))
    print(C)
else:
    print("khong hop le")
