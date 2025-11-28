# cau5.py
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Symbolic
x = sp.symbols('x', real=True)
y = x**3 - 6*x**2 + 9*x + 2

y_prime = sp.diff(y, x)
y_double = sp.diff(y_prime, x)
crit_points = sp.solve(sp.Eq(y_prime, 0), x)

print("Hàm y =", y)
print("Đạo hàm y' =", y_prime)
print("Nghiệm y'=0 (điểm tới hạn):", crit_points)

for cp in crit_points:
    val = y.subs(x, cp)
    conc = y_double.subs(x, cp)
    typ = "cực đại" if conc < 0 else ("cực tiểu" if conc > 0 else "điểm yên ngựa")
    print(f" x = {cp}: y = {sp.N(val)}, y'' = {sp.N(conc)} => {typ}")

print("\nKết luận:")
print(" - Local max: x=1, y=6")
print(" - Local min: x=3, y=2")
print(" - Không có max toàn cục hoặc min toàn cục (hàm unbounded vì bậc 3).")

# Numeric check & plot
xs = np.linspace(-2, 6, 400)
ys = xs**3 - 6*xs**2 + 9*xs + 2

plt.figure(figsize=(8,4))
plt.plot(xs, ys, label='y(x)')
plt.scatter([1,3], [6,2], color='red', zorder=5, label='critical points')
plt.axhline(0, linewidth=0.5)
plt.title("Đồ thị y = x^3 -6x^2 +9x +2 (vùng [-2,6])")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
