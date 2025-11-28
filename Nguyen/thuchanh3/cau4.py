import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')

# Biểu thức
expr = sp.sqrt(x**2 + 3 - 2*x) / ((x + 6 + 2*x - 1)**(1/3))


limit_val = sp.limit(expr, x, 2)
print("Giá trị giới hạn =", limit_val)

# Vẽ đồ thị trong khoảng [5, 30]
x_vals = np.linspace(5, 30, 400)
y_vals = np.sqrt(x_vals**2 + 3 - 2*x_vals) / ((x_vals + 6 + 2*x_vals - 1)**(1/3))

plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label="Hàm f(x)")
plt.title("Đồ thị hàm số trong khoảng [5,30]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
