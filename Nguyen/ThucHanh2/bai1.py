import numpy as np
k = int(input("nhap k tu ban phim"))

A = np.random.randint(-10,11,(k,k))
B = np.random.randint(-10,11,(k,k))

print("ma tran A \n")
print(A)
print("\n Ma tran B")
print(B)

# a,
print("A + B")
print(A+B)
print("\n A-B")
print(A-B)
print("\n A*B")
print(A*B)
print("\n A/B")
print(A/B)

#b,
print("\n phep nhan tich vo huong ")
print(A@B)

#c,
d = int(input("nhap k "))
print(f"A^{d} = ")
print(np.linalg.matrix_power(A,d))

#d,
print("ma tran chuyen vi la ")
print(A.T)

#e, tinh dinh thuc
print("dinh thuc")
detA = np.linalg.det(A)
detB = np.linalg.det(B)

print(f"\n{detA}")
print(f"\n{detB}")
