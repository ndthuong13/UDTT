# cau5_fixed.py
import numpy as np
import matplotlib.pyplot as plt

def Y(x):
    return np.sin(x)**2 + x**4 + 100

# 1) Lý luận: min toàn cục = 100 tại x = 0; hàm không có max (tới +inf khi |x|->inf)
print("Lý luận phân tích:")
print(" - Vì sin^2(x) >= 0 và x^4 >= 0, nên Y(x) >= 100.")
print(" - Tại x = 0, Y(0) = 100 --> giá trị nhỏ nhất toàn cục là 100 tại x = 0.")
print(" - Vì x^4 -> +inf khi |x| -> +inf, Y không có giá trị lớn nhất (unbounded above).")
print()

# 2) Kiểm tra số học trên một đoạn hữu hạn [-L, L] (để minh chứng)
L = 10
xs = np.linspace(-L, L, 200000)  # lưới rất mịn để tìm min chính xác gần đúng
ys = Y(xs)

idx_min = np.argmin(ys)
x_min_approx = xs[idx_min]
y_min_approx = ys[idx_min]

idx_max = np.argmax(ys)
x_max_approx = xs[idx_max]
y_max_approx = ys[idx_max]

print("Kiểm tra số học trên đoạn [{:.1f},{:.1f}]:".format(-L, L))
print(f" - Giá trị nhỏ nhất x ≈ {x_min_approx:.8f}, Y ≈ {y_min_approx:.12f}")
print(f"   (So sánh với giá trị lý thuyết Y(0)=100)")

print(f" - Giá trị lớn nhất trên đoạn (hữu hạn) x ≈ {x_max_approx:.8f}, Y ≈ {y_max_approx:.6e}")
print("   (Lưu ý: trên đoạn hữu hạn ta có max; nhưng trên toàn R hàm unbounded above.)")

# 3) Vẽ đồ thị để quan sát
plt.figure(figsize=(9,5))
xs_plot = np.linspace(-3, 3, 1000)
plt.plot(xs_plot, Y(xs_plot), label=r'$Y=\sin^2(x)+x^4+100$')
plt.scatter([0], [Y(0)], color='red', zorder=5, label='Min ở x=0, Y=100')
plt.title("Đồ thị gần quanh min (x trong [-3,3])")
plt.xlabel("x")
plt.ylabel("Y(x)")
plt.grid(True)
plt.legend()
plt.show()
