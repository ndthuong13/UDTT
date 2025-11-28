import numpy as np


def myfunc(A):
    """
    Tính tổng độ biến động của tất cả các hàng trong ma trận
    Độ biến động = giá trị lớn nhất - giá trị nhỏ nhất trong mỗi hàng
    """
    # Tính độ biến động cho từng hàng
    fluctuations = np.max(A, axis=1) - np.min(A, axis=1)

    # Tính tổng độ biến động của tất cả các hàng
    total_fluctuation = np.sum(fluctuations)

    return total_fluctuation


def main():
    # Ví dụ sử dụng
    print("Ví dụ 1:")
    A1 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
    print("Ma trận A1:")
    print(A1)
    result1 = myfunc(A1)
    print(f"Tổng độ biến động: {result1}")

    print("\n" + "=" * 40)

    print("Ví dụ 2:")
    A2 = np.array([[10, -5, 20],
                   [3, 3, 3],
                   [15, 8, 25]])
    print("Ma trận A2:")
    print(A2)
    result2 = myfunc(A2)
    print(f"Tổng độ biến động: {result2}")

    print("\n" + "=" * 40)

    # Tạo ma trận ngẫu nhiên
    m = int(input("Nhập số dòng m: "))
    n = int(input("Nhập số cột n: "))

    A_random = np.random.randint(-50, 51, (m, n))
    print("\nMa trận ngẫu nhiên:")
    print(A_random)

    result_random = myfunc(A_random)
    print(f"Tổng độ biến động: {result_random}")

    # Hiển thị chi tiết từng hàng
    print("\nChi tiết từng hàng:")
    for i in range(m):
        row = A_random[i]
        fluctuation = np.max(row) - np.min(row)
        print(f"Hàng {i}: min={np.min(row)}, max={np.max(row)}, độ biến động={fluctuation}")


# Phiên bản không dùng numpy
def myfunc_no_numpy(matrix):
    """
    Phiên bản không sử dụng numpy
    """
    total_fluctuation = 0

    for row in matrix:
        min_val = min(row)
        max_val = max(row)
        fluctuation = max_val - min_val
        total_fluctuation += fluctuation

    return total_fluctuation


if __name__ == "__main__":
    main()

    # Ví dụ thêm với phiên bản không dùng numpy
    print("\n" + "=" * 50)
    print("Ví dụ với phiên bản không dùng numpy:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = myfunc_no_numpy(matrix)
    print(f"Ma trận: {matrix}")
    print(f"Tổng độ biến động: {result}")