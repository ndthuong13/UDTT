import numpy as np
import pandas as pd
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from scipy.fftpack import dct

df = pd.read_csv("Iris.csv").sample(frac=1, random_state=42)
X = df.iloc[:, :-1].values.astype(float)
y = df.iloc[:, -1].values

# # Chuẩn hóa Standardize
# X = (X - X.mean(axis=0)) / X.std(axis=0)
# X = dct(X, axis=1, norm="ortho")  # DCT

# Min–Max Scaling
# min_val = X.min(axis=0)
# max_val = X.max(axis=0)
# X = (X - min_val) / (max_val - min_val)

# Normalize (L2)
# norm = np.sqrt(np.sum(X**2, axis=1, keepdims=True))
# X = X / norm

#Z-score (công thức khác Standardize)
median = np.median(X, axis=0)
q1 = np.percentile(X, 25, axis=0)
q3 = np.percentile(X, 75, axis=0)
iqr = q3 - q1
X = (X - median) / iqr

# Perceptron train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
pred = Perceptron(max_iter=2000).fit(X_train, y_train).predict(X_test)
print("\nPerceptron")
print("Acc:", accuracy_score(y_test,pred), "Prec:", precision_score(y_test,pred,average='macro',zero_division=0),
      "Rec:", recall_score(y_test,pred,average='macro',zero_division=0), "F1:", f1_score(y_test,pred,average='macro',zero_division=0))

# K-Fold SVM & Logistic
kf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
acc_svm, acc_log = [], []

for tr, te in kf.split(X, y):
    Xtr, Xte = X[tr], X[te]; ytr, yte = y[tr], y[te]
    acc_svm.append(accuracy_score(yte, SVC().fit(Xtr,ytr).predict(Xte)))
    acc_log.append(accuracy_score(yte, LogisticRegression(max_iter=2000).fit(Xtr,ytr).predict(Xte)))

print("\nK-Fold")
print("SVM Acc:", np.mean(acc_svm), "Logistic Acc:", np.mean(acc_log))
