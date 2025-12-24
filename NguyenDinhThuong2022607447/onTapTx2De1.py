import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# df = pd.read_csv('wine.data', header=None)
# 0. Giả lập/Đọc dữ liệu
# df = pd.read_csv('cpu.csv')
# Dưới đây là dữ liệu mẫu để chạy demo:
data = np.random.rand(200, 6)
df = pd.DataFrame(data, columns=['col1', 'col2', 'col3', 'col4', 'col5', 'class'])
df['class'] = np.random.choice(['High', 'Low', 'Medium'], 200)

print("--- Dữ liệu gốc (5 dòng đầu) ---")
print(df.head())

# --- CÂU 1: Chuẩn hóa dữ liệu ---
# Chuẩn hóa 2 cột đầu về [0, 1]
scaler_minmax = MinMaxScaler()
df.iloc[:, 0:2] = scaler_minmax.fit_transform(df.iloc[:, 0:2])

# Chuẩn hóa các cột còn lại (trừ cột class) theo Standardize (Z-score)
scaler_std = StandardScaler()
cols_to_std = df.columns[2:-1]
df[cols_to_std] = scaler_std.fit_transform(df[cols_to_std])

# Số hóa cột class
le = LabelEncoder()
df['class'] = le.fit_transform(df['class'])

# --- CÂU 2: Biến đổi Fourier (FFT) cho 10 dòng đầu ---
data_10 = df.iloc[:10, :-1].values
fft_forward = np.fft.fft(data_10)
fft_inverse = np.fft.ifft(fft_forward)

print("\n--- Câu 2: Biến đổi Fourier (Dòng đầu tiên) ---")
print("Trước biến đổi:", data_10[0])
print("Biến đổi thuận (FFT):", fft_forward[0])
print("Biến đổi nghịch (IFFT):", fft_inverse[0].real)

# --- CÂU 3: Chia dữ liệu 95% Train, 5% Test ---
X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=42)

# --- CÂU 4 & 5 & 6: K-Fold 5 và Phân lớp ---
kf = KFold(n_splits=5, shuffle=True, random_state=42)


def evaluate_model(model, name):
    accs, precs, recs = [], [], []

    print(f"\n--- Kết quả mô hình {name} ---")
    fold = 1
    for train_index, val_index in kf.split(X_train):
        # Chia fold trong bộ train
        X_tr, X_val = X_train.iloc[train_index], X_train.iloc[val_index]
        y_tr, y_val = y_train.iloc[train_index], y_train.iloc[val_index]

        # Huấn luyện
        model.fit(X_tr, y_tr)
        y_pred = model.predict(X_val)

        # Tính metrics cho từng fold
        accs.append(accuracy_score(y_val, y_pred))
        precs.append(precision_score(y_val, y_pred, average='macro', zero_division=0))
        recs.append(recall_score(y_val, y_pred, average='macro', zero_division=0))
        fold += 1

    # Đánh giá trên bộ TEST (Câu 5 & 6)
    y_test_pred = model.predict(X_test)
    correct = sum(y_test_pred == y_test)
    incorrect = len(y_test) - correct
    print(f"Trên bộ Test: Đúng {correct}, Sai {incorrect}")

    return accs, precs, recs


# Thực hiện cho Bayes và KNN
metrics_bayes = evaluate_model(GaussianNB(), "Bayes")
metrics_knn = evaluate_model(KNeighborsClassifier(n_neighbors=5), "KNN")


# --- CÂU 7: Hiển thị kết quả và Đồ thị ---
def plot_metrics(metrics, title):
    labels = ['Fold 1', 'Fold 2', 'Fold 3', 'Fold 4', 'Fold 5']
    x = np.arange(len(labels))

    plt.figure(figsize=(10, 5))
    plt.plot(labels, metrics[0], marker='o', label=f'Accuracy (Avg: {np.mean(metrics[0]):.2f})')
    plt.plot(labels, metrics[1], marker='s', label=f'Precision (Avg: {np.mean(metrics[1]):.2f})')
    plt.plot(labels, metrics[2], marker='^', label=f'Recall (Avg: {np.mean(metrics[2]):.2f})')

    plt.title(f'Metrics per Fold - {title}')
    plt.ylabel('Score')
    plt.legend()
    plt.grid(True)
    plt.show()


plot_metrics(metrics_bayes, "Bayes")
plot_metrics(metrics_knn, "KNN")