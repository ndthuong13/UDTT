import numpy as np

A = np.array([
    [3.2, 2.8, 4.1, 5.2, 1.9],
    [2.5, 4.3, 3.8, 5.6, 2.7],
    [4.8, 3.7, 5.5, 6.1, 3.9],
    [2.9, 3.4, 4.0, 5.7, 2.8],
    [3.1, 2.9, 3.6, 4.2, 2.5]
])

# Tính trị riêng và vector riêng
eigvals, eigvecs = np.linalg.eig(A)

print("Các trị riêng (eigenvalues):")
print(eigvals)

print("\nCác vector riêng (eigenvectors):")
print(eigvecs)
