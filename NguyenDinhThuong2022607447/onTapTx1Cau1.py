import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

A = np.array([
    [-1.4, 1.1, 2.2, -1.5, 2.1, 3.2],
    [1.1, 1.5, -2.1, 3.5, 4.6, 2.2],
    [-2.2, 2.1, 1.1, 3.3, -4.2, 2.8],
    [1.5, -3.5, 3.3, 1.3, 1.2, -4.8],
    [2.1, 4.6, -4.2, 1.2, -2.5, 1.6],
    [3.2, 2.2, 2.8, 4.8, 1.6, 1.2]
])
#Tinh dinh thuc, tim ma tran nghich dao
det_A = np.linalg.det(A)
inv_A = np.linalg.inv(A)
print("\nDinh thuc cua ma tran A: ", det_A)
print("\nMa tran nghich dao cua A: ", inv_A)

#Tim B gap 5 lan A
B = 5 * A
print("\nMa tran B: ", B)
#Tim A^2
C = A @ A
print("\nMa tran A x A: ", C)
#Tim ma tran chuyen vi cua A
F = A.T
print("\nMa tran chuyen vi cua A: ", F)

#Tim Tong so phan tu lon hon trung binh cong cua A
tbc = np.mean(A)
count = np.sum(A > tbc)
print("\nTong cac phan tu lon hon trung binh cong cua A: ", count)

#Tong so phan tu am cua A
negative = np.sum(A < 0)
print("\nTong cac phan tu am cua A la: ", negative)

#Tim tong max cac hang cua A
row_maxes = np.max(A, axis=1)
C = np.sum(row_maxes)
print("\nTong cac gia tri lon nhat cua moi hang: ", C)

#Tim tong min cac cot cua A
row_mins = np.min(A, axis=0)
D = np.sum(row_mins)
print("\nTong cac gia tri nho nhat cua cac cot: ", D)

#Tim gia tri rieng, vector rieng
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nGia tri rieng cua A: ", eigenvalues)
print("\nVector rieng cua A: \n", eigenvectors)

#Giai he phuong trinh
D = np.array([[2, -3], [1, 4]])
B = np.array([1, 6])
sold_d = np.linalg.solve(D, B)
print("\nNghiem cua he phuong trinh la: ",sold_d[0], " va ", sold_d[1])

# Tim dao ham
def f(x):
    return x**5 - 3*x**2 + 6*x - 10

x = sp.symbols('x')
fx = x**5 - 3*x**2 + 6*x - 10
f_prime = sp.diff(fx, x)
print(f"\nDao ham cua ham so {fx} la: ", f_prime)

#Ve do thi cua cac ham so
x_vals = np.linspace(-100, 100, 1000)
y_vals = f(x_vals)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label='f(x) = x**5 - 3*x**2 + 6*x - 10', color='red')
plt.title('Do thi ham so f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()