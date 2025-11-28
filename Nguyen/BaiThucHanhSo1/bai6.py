import math

def F(x,n):
    if n < 20:
        tong = 0
        mau = 0
        for i in range(1,n+1):
            mau = mau+i
            tong += x-1/mau
        return tong
    else:
        return math.sqrt(n)+x

x, n = map(int, input("Nhập x và n (cách nhau bởi khoảng trắng): ").split())

print("ket qua F(x,n)",F(x,n))


