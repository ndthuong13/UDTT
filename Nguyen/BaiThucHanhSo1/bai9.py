import math

n = int(input("nhap n "))
sum = 0

for i in range(1,n+1):
    sum += 1/math.pow(i,2)

print(sum)