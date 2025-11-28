import numpy as np

def minkowski(x, y, p=2):
    return np.sum(np.abs(np.array(x) - np.array(y)) ** p) ** (1/p)

def manhattan(x, y):
    return np.sum(np.abs(np.array(x) - np.array(y)))

def euclidean(x, y):
    return np.linalg.norm(np.array(x) - np.array(y))

# Ví dụ sử dụng
x = [1, 2, 3]
y = [4, 5, 6]

print(f"Manhattan: {manhattan(x, y):.2f}")
print(f"Euclidean: {euclidean(x, y):.2f}")
print(f"Minkowski p=3: {minkowski(x, y, 3):.2f}")