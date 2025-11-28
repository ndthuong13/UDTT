import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


x = sp.Symbol('x')
y = x**3 + 10*sp.cos(x)**2


y_prime = sp.diff(y, x)
print("Đạo hàm y'(x) =", y_prime)


x_vals = np.linspace(-20, 20, 400)
y_vals = x_vals**3 + 10*np.cos(x_vals)**2
y_prime_vals = 3*x_vals**2 - 20*np.cos(x_vals)*np.sin(x_vals)

plt.figure(figsize=(10,5))
plt.plot(x_vals, y_vals, label='y = x^3 + 10cos²(x)')
plt.plot(x_vals, y_prime_vals, label="y' = 3x² - 20cos(x)sin(x)", linestyle='--')
plt.title("Đồ thị hàm và đạo hàm của y = x³ + 10cos²(x)")
plt.xlabel("x")
plt.ylabel("Giá trị")
plt.legend()
plt.grid(True)
plt.show()
