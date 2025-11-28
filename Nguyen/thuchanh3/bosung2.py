import sympy as sp

x = sp.Symbol('x')

# Tích phân 1
expr1 = sp.sin(x) + 3*sp.cos(x)
I1 = sp.integrate(expr1, (x, 0, sp.pi/2))

# Tích phân 2
expr2 = (x**2 - 1)/(x**3 + x)
I2 = sp.integrate(expr2, (x, 1, 4))

print("Giá trị tích phân 1 =", float(I1))
print("Giá trị tích phân 2 =", float(I2))
