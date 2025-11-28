import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
expr = (sp.sqrt(x**2 + 5) - 4)/(x - 3)

# Tính giới hạn tại x → 3
limit_val = sp.limit(expr, x, 3)
print("Giá trị giới hạn =", limit_val)

# Vẽ đồ thị
x_vals = np.linspace(1, 6, 400)
y_vals = (np.sqrt(x_vals**2 + 5) - 4) / (x_vals - 3)

plt.figure(figsize=(8,5))
plt.plot(x_vals, y_vals, label="f(x) = (√(x² + 5) - 4)/(x - 3)")
plt.axvline(3, color='r', linestyle='--', label='x = 3')
plt.title("Đồ thị hàm số f(x) trong khoảng [1, 6]")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
