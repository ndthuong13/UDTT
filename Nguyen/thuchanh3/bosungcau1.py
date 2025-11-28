import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
y = sp.exp(-x/5) * sp.cos(2*x)

# Đạo hàm
y_prime = sp.diff(y, x)
print("Đạo hàm y'(x) =", y_prime)

# Vẽ đồ thị
x_vals = np.linspace(-10, 10, 400)
y_vals = np.exp(-x_vals/5) * np.cos(2*x_vals)
y_prime_vals = np.exp(-x_vals/5)*(-2*np.sin(2*x_vals) - (1/5)*np.cos(2*x_vals))

plt.figure(figsize=(9,5))
plt.plot(x_vals, y_vals, label='y = e^(-x/5)*cos(2x)')
plt.plot(x_vals, y_prime_vals, '--', label="y' (đạo hàm)")
plt.title("Đồ thị hàm và đạo hàm của y = e^(-x/5)*cos(2x)")
plt.xlabel("x")
plt.ylabel("Giá trị")
plt.grid(True)
plt.legend()
plt.show()
