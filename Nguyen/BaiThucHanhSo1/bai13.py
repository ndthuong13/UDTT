import math


def D(x,n):
    result1 = (math.sin(n*x))/1+math.cos(x)**2
    result2 = (x + 1) ** (1/n)
    result = result1 + result2
    return result

x, n = map(float, input("Nhập x và n: ").split())
print(D(x,n))