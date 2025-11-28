import numpy as np

# Tạo ma trận A kích thước mxn và vector B độ dài n
m, n = 3, 4
A = np.random.randint(1, 5, (m, n))
B = np.random.randint(1, 5, n)

print("Ma trận A (3x4):")
print(A)
print(f"\nVector B (độ dài {n}): {B}")

result = A @ B  # hoặc np.dot(A, B)
print(f"\nA * B = {result}")

# Giải thích chi tiết
print("\nGiải thích:")
for i in range(m):
    row_result = sum(A[i,j] * B[j] for j in range(n))
    print(f"Hàng {i}: {A[i]} · {B} = {row_result}")