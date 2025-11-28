import numpy as np


A = np.array([
    [5.4, 3.1, 6.2, 1.5, 6.1, 3.2],
    [5.1, 8.5, 8.1, 3.5, 4.6, 2.2],
    [6.2, 2.1, 3.3, 3.3, 4.2, 5.8],
    [6.5, 3.5, 3.3, 3.3, 8.2, 4.8],
    [4.3, 4.2, 4.2, 8.2, 5.6, 1.8],
    [3.2, 8.2, 5.1, 4.8, 5.6, 8.2]
])


eigvals, eigvecs = np.linalg.eig(A)

print("Các trị riêng (Eigenvalues):")
print(eigvals)

print("\nCác vectơ riêng (Eigenvectors):")
print(eigvecs)
