import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split, KFold
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# --- Bước 0: Giả lập hoặc Đọc dữ liệu ---
# df = pd.read_csv('wine.csv')
# Giả lập dữ liệu wine (thường có 13-14 cột thuộc tính và 1 cột class)
num_samples = 200
num_features = 10
data = np.random.rand(num_samples, num_features) * 100
df = pd.DataFrame(data, columns=[f'feat_{i}' for i in range(num_features)])
df['class'] = np.random.choice(['Type A', 'Type B', 'Type C'], num_samples)

# --- Câu a: Chuẩn hóa dữ liệu ---
# 4 cột đầu về [0, 10]
scaler_0_10 = MinMaxScaler(feature_range=(0, 10))
df.iloc[:, 0:4] = scaler_0_10.fit_transform(df.iloc[:, 0:4])

# Các cột còn lại (trừ class) chuẩn hóa (Normalize - thường là MinMax [0,1])
scaler_norm = MinMaxScaler(feature_range=(0, 1))
cols_remaining = df.columns[4:-1]
df[cols_remaining] = scaler_norm.fit_transform(df[cols_remaining])

# Số hóa cột class
le = LabelEncoder()
df['class'] = le.fit_transform(df['class'])

# --- Câu b: Biến đổi Cosin (DCT) cho 5 dòng đầu ---
data_5 = df.iloc[:5, :-1].values
dct_forward = dct(data_5, axis=1, type=2)
dct_inverse = idct(dct_forward, axis=1, type=2) / (2 * data_5.shape[1])

print("--- Câu b: Biến đổi Cosin (Dòng 1) ---")
print(f"Gốc: {data_5[0][:3]}...")
print(f"Thuận: {dct_forward[0][:3]}...")
print(f"Nghịch: {dct_inverse[0][:3]}...\n")

# --- Câu c: Chia dữ liệu 97% Train, 3% Test ---
X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.03, random_state=42)

# --- Câu d, e, f: K-Fold 10 và Phân lớp SVM, Logistic ---
kf = KFold(n_splits=10, shuffle=True, random_state=42)


def process_model(model, name):
    accs, precs, recs = [], [], []

    # Huấn luyện trên 10-fold của bộ Train
    for train_idx, val_idx in kf.split(X_train):
        X_tr, X_val = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_tr, y_val = y_train.iloc[train_idx], y_train.iloc[val_idx]

        model.fit(X_tr, y_tr)
        y_pred = model.predict(X_val)

        accs.append(accuracy_score(y_val, y_pred))
        precs.append(precision_score(y_val, y_pred, average='macro', zero_division=0))
        recs.append(recall_score(y_val, y_pred, average='macro', zero_division=0))

    # Xác định độ chính xác trên bộ TEST (Câu e, f)
    y_test_pred = model.predict(X_test)
    test_acc = accuracy_score(y_test, y_test_pred)
    print(f"Độ chính xác {name} trên bộ Test: {test_acc:.2%}")

    return accs, precs, recs


metrics_svm = process_model(SVC(kernel='linear'), "SVM")
metrics_logistic = process_model(LogisticRegression(max_iter=1000), "Logistic")


# --- Câu g: Hiển thị kết quả và Đồ thị ---
def visualize(metrics, title):
    folds = range(1, 11)
    plt.figure(figsize=(10, 5))
    plt.plot(folds, metrics[0], 'o-', label='Accuracy')
    plt.plot(folds, metrics[1], 's-', label='Precision')
    plt.plot(folds, metrics[2], 'd-', label='Recall')

    plt.axhline(y=np.mean(metrics[0]), color='r', linestyle='--', label=f'Mean Acc: {np.mean(metrics[0]):.2f}')
    plt.title(f'Kết quả 10-Fold của {title}')
    plt.xlabel('Lần Train (Fold)')
    plt.ylabel('Giá trị')
    plt.legend()
    plt.grid(True)
    plt.show()


visualize(metrics_svm, "SVM")
visualize(metrics_logistic, "Logistic")