import math

n = int(input("nhap n "))
#cach 1
result1 = 1
for i in range(1,n+1):
    result1*=i
print(result1)

#cach 2
result2 = math.factorial(n)
print(result2)
    