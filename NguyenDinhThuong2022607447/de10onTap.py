import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_validate, StratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score

# 1. Khởi tạo dữ liệu từ bảng
data = {
    'A': [1.4, 1.1, 2.2, 1.5, 2.1, 9.2, 19.1, 2.2, 9.1, 19.0],
    'B': [1.1, 1.5, 2.1, 9.5, 4.6, 2.2, 2.9, 4.2, 2.1, 2.1],
    'C': [92.2, 12.1, 21.1, 23.3, 34.2, 52.8, 3.8, 34.1, 52.1, 3.1],
    'D': [1.5, 3.5, 3.3, 1.3, 1.2, 4.8, 6.1, 1.4, 4.1, 4.1],
    'E': [2.1, 4.6, 4.2, 1.2, 2.5, 1.6, 3.2, 2.2, 1.1, 4.2],
    'F': [3.2, 2.2, 2.8, 4.8, 1.6, 1.2, 8.9, 1.1, 1.1, 4.9],
    'G': [12.4, 15.1, 26.2, 13.5, 21.1, 3.2, 9.1, 21.9, 3.1, 4.1],
    'CLASS': [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
}

df = pd.DataFrame(data)
X = df.drop('CLASS', axis=1)
y = df['CLASS']

# --- CÂU A: Chuẩn hóa dữ liệu về [0, 1] ---
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# --- CÂU B: Chia dữ liệu ---
# Tách riêng tập Test 40% (4 mẫu) theo yêu cầu
X_train_full, X_test, y_train_full, y_test = train_test_split(
    X_scaled, y, test_size=0.4, random_state=42, stratify=y
)

# Thiết lập bộ chia 5-fold (Vì chỉ có 10 mẫu tổng cộng, mỗi fold sẽ có 2 mẫu)
cv_stratified = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Định nghĩa hàm đo lường có xử lý lỗi chia cho 0 (zero_division=0)
scoring = {
    'accuracy': 'accuracy',
    'precision': make_scorer(precision_score, average='macro', zero_division=0),
    'recall': make_scorer(recall_score, average='macro', zero_division=0)
}

# --- CÂU C & D: Huấn luyện Bayes và SVM ---
models = {
    'Bayes (GaussianNB)': GaussianNB(),
    'SVM': SVC(kernel='linear', C=1.0)
}

results_list = []

for name, model in models.items():
    # Thực hiện 5-fold cross validation trên toàn bộ dữ liệu đã chuẩn hóa
    cv_results = cross_validate(model, X_scaled, y, cv=cv_stratified, scoring=scoring)

    results_list.append({
        'Model': name,
        'Accuracy': np.mean(cv_results['test_accuracy']),
        'Precision': np.mean(cv_results['test_precision']),
        'Recall': np.mean(cv_results['test_recall'])
    })

# --- CÂU E: Hiển thị kết quả ---
results_df = pd.DataFrame(results_list)
print("\n--- BẢNG KẾT QUẢ ĐÁNH GIÁ (TRUNG BÌNH 5-FOLD) ---")
print(results_df.to_string(index=False))

# Vẽ đồ thị so sánh các chỉ số
results_df.set_index('Model').plot(kind='bar', figsize=(10, 5))
plt.title('Hiệu suất mô hình Bayes vs SVM (Dữ liệu chuẩn hóa)')
plt.ylabel('Giá trị (0.0 - 1.0)')
plt.xticks(rotation=0)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
