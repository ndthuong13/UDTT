# cau6.py
import sympy as sp

# ẩn
x, y, z = sp.symbols('x y z')

# Hệ 1
eqs1 = [
    sp.Eq(2*x - y + z, 5),
    sp.Eq(x + 3*y - 2*z, 4),
    sp.Eq(3*x + y + z, 10)
]

sol1 = sp.solve(eqs1, (x, y, z))
print("Nghiệm hệ 1:")
print(sol1)

# Kiểm tra thay ngược
print("\nKiểm tra hệ 1 (thay nghiệm vào các phương trình):")
for eq in eqs1:
    print(sp.simplify(eq.lhs.subs(sol1) - eq.rhs))

# Hệ 2
eqs2 = [
    sp.Eq(x + 2*y - z, 6),
    sp.Eq(3*x - y + 4*z, 8),
    sp.Eq(x + y + z, 5)
]

sol2 = sp.solve(eqs2, (x, y, z))
print("\nNghiệm hệ 2:")
print(sol2)

# Kiểm tra thay ngược
print("\nKiểm tra hệ 2 (thay nghiệm vào các phương trình):")
for eq in eqs2:
    print(sp.simplify(eq.lhs.subs(sol2) - eq.rhs))
