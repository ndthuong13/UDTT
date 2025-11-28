import numpy as np

# Tạo ma trận A kích thước mxn
m, n = 3, 4
A = np.random.randint(1, 10, (m, n))
b = 2

print("Ma trận A:")
print(A)
print(f"\nSố vô hướng b = {b}")

print(f"\nA + b = \n{A + b}")
print(f"\nA - b = \n{A - b}")
print(f"\nA * b = \n{A * b}")
print(f"\nA / b = \n{A / b}")
print(f"\nA % b = \n{A % b}")