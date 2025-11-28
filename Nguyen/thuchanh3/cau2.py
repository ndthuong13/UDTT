import sympy as sp

x = sp.Symbol('x')


expr1 = sp.exp(x) + 4
I1 = sp.integrate(expr1, (x, 1, 3))


expr2 = 1/(x+1) - 1/(x+2)
I2 = sp.integrate(expr2, (x, 0, 1))

print("Giá trị tích phân 1 =", float(I1))
print("Giá trị tích phân 2 =", float(I2))
