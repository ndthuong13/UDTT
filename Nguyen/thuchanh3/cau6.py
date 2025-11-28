import sympy as sp

# Khai báo ẩn số
x, y, z = sp.symbols('x y z')

# Hệ 1
eqs1 = [
    sp.Eq(x - y + 2*z, 4),
    sp.Eq(2*x + y - z, -1),
    sp.Eq(x + y + z, 5)
]

sol1 = sp.solve(eqs1, (x, y, z))
print("🔹 Nghiệm hệ 1:")
print(sol1)

# Hệ 2
eqs2 = [
    sp.Eq(5*x - y + 2*z, 20),
    sp.Eq(2*x + 2*y - z, 23),
    sp.Eq(x + y - z, 11)
]

sol2 = sp.solve(eqs2, (x, y, z))
print("\n🔹 Nghiệm hệ 2:")
print(sol2)
