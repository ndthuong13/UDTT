import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier

### Bài 1: Perceptron cho phân loại nhị phân

X1 = np.array([
    [1, 1],
    [8, 3],
    [2, 7],
    [8, 8],
    [9, 9]
])
y1 = np.array([0, 0, 1, 1, 1])

perceptron1 = Perceptron(random_state=42, eta0=1.0)
perceptron1.fit(X1, y1)

du_lieu_test1 = np.array([[9, 2]])
ket_qua_test1 = perceptron1.predict(du_lieu_test1)

print("--- Bài 1: Perceptron đơn ---")
print(perceptron1.predict(X1))
print(f"Dự đoán cho [9, 2]: {ket_qua_test1[0]}")


### Bài 2: MLPClassifier cho phân loại đa lớp

X2 = np.array([
    [1, 1],
    [2, 2],
    [8, 1],
    [9, 3],
    [2, 7],
    [3, 8],
    [8, 8],
    [9, 9]
])
y2_label = np.array(['00', '00', '10', '10', '01', '01', '11', '11'])

du_lieu_test2 = np.array([[9, 2]])

mlp2 = MLPClassifier(hidden_layer_sizes=(10,), max_iter=1000, random_state=42)
mlp2.fit(X2, y2_label)

ket_qua_test2 = mlp2.predict(du_lieu_test2)

print("\n--- Bài 2: Mạng Noron Đa Lớp (MLP) ---")
print(mlp2.predict(X2))
print(f"Dự đoán cho [9, 2]: {ket_qua_test2[0]}")