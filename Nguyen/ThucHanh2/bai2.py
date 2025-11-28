import numpy as np
m,n = map(int,input("nhap m va n ").split())

A = np.random.randint(-100,101,(m,n))

print("\nTOÀN MA TRẬN:")
print(A.sum())
print(A.min())
print(A.max())
print(A.mean())


print("dong")
for i in range(m):
    row = A[i]
    print(row.sum())
    print(row.min())
    print(row.max())
    print(row.mean())

print("cot")
for j in range(n):
    col = A[:,j]
    print(col.sum())
    print(col.min())
    print(col.max())
    print(col.mean())




