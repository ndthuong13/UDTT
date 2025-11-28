import numpy as np

# Tạo vector độ dài 50
vector = np.arange(50)

# Reshape thành ma trận 5x10
matrix = vector.reshape(5, 10)

print("Vector gốc (50 phần tử):")
print(vector)
print(f"\nShape: {vector.shape}")

print("\nMa trận sau khi reshape (5x10):")
print(matrix)
print(f"Shape: {matrix.shape}")