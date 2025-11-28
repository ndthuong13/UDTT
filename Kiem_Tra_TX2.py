import numpy as np
import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from scipy.fftpack import dct

# 1. LOAD DATA
df = pd.read_csv("Iris.csv")

# Xáo trộn dữ liệu
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

X = df.iloc[:, :-1].values.astype(float)
y = df.iloc[:, -1].values

# 2. CHUẨN HOÁ (STANDARDIZE)
# Standardize: (x - mean) / std
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std

# Min–Max Scaling
# min_val = X.min(axis=0)
# max_val = X.max(axis=0)
# X = (X - min_val) / (max_val - min_val)

# Normalize (L2)
# norm = np.sqrt(np.sum(X**2, axis=1, keepdims=True))
# X = X / norm

#Z-score (công thức khác Standardize)
# median = np.median(X, axis=0)
# q1 = np.percentile(X, 25, axis=0)
# q3 = np.percentile(X, 75, axis=0)
# iqr = q3 - q1
# X = (X - median) / iqr

# 3. DCT BIẾN ĐỔI COSIN
X = dct(X, axis=1, norm="ortho")

# 4. CHIA TRAIN/TEST = PERCEPTRON (stratify để tránh lớp trống)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model_per = Perceptron(max_iter=2000)
model_per.fit(X_train, y_train)
pred_per = model_per.predict(X_test)

print("\nKẾT QUẢ PERCEPTRON (Train/Test)")
print("Accuracy:", accuracy_score(y_test, pred_per))
print("Precision:", precision_score(y_test, pred_per, average='macro', zero_division=0))
print("Recall:", recall_score(y_test, pred_per, average='macro', zero_division=0))
print("F1:", f1_score(y_test, pred_per, average='macro', zero_division=0))

# 5. K-FOLD VỚI SVM & LOGISTIC (Stratified)
k = 5
kf = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)

acc_svm = []
prec_svm = []
rec_svm = []
f1_svm = []

acc_log = []
prec_log = []
rec_log = []
f1_log = []

for train_idx, test_idx in kf.split(X, y):
    Xtr, Xte = X[train_idx], X[test_idx]
    ytr, yte = y[train_idx], y[test_idx]

    # SVM
    svm = SVC()
    svm.fit(Xtr, ytr)
    pred1 = svm.predict(Xte)
    acc_svm.append(accuracy_score(yte, pred1))
    prec_svm.append(precision_score(yte, pred1, average='macro', zero_division=0))
    rec_svm.append(recall_score(yte, pred1, average='macro', zero_division=0))
    f1_svm.append(f1_score(yte, pred1, average='macro', zero_division=0))

    # Logistic Regression
    log = LogisticRegression(max_iter=2000)
    log.fit(Xtr, ytr)
    pred2 = log.predict(Xte)
    acc_log.append(accuracy_score(yte, pred2))
    prec_log.append(precision_score(yte, pred2, average='macro', zero_division=0))
    rec_log.append(recall_score(yte, pred2, average='macro', zero_division=0))
    f1_log.append(f1_score(yte, pred2, average='macro', zero_division=0))

print("\nKẾT QUẢ K-FOLD")
print("SVM - Accuracy:", np.mean(acc_svm), "Precision:", np.mean(prec_svm), "Recall:", np.mean(rec_svm), "F1:", np.mean(f1_svm))
print("Logistic - Accuracy:", np.mean(acc_log), "Precision:", np.mean(prec_log), "Recall:", np.mean(rec_log), "F1:", np.mean(f1_log))
