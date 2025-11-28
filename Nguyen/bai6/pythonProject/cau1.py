import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import CategoricalNB

# Đọc file Excel
df = pd.read_excel("data1.xlsx")

# Hiển thị dữ liệu
print("📘 Dữ liệu đọc được:")
print(df.head(), "\n")

# Chia dữ liệu: X là đặc trưng, y là nhãn
X = df.drop(["ID", "Buy"], axis=1)
y = df["Buy"]

# Mã hóa dữ liệu dạng chữ thành số
encoders = {}
for col in X.columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    encoders[col] = le

label_y = LabelEncoder()
y_encoded = label_y.fit_transform(y)

# Huấn luyện mô hình Naive Bayes
model = CategoricalNB()
model.fit(X, y_encoded)

# Xác suất của từng mẫu trong dữ liệu gốc
probs = model.predict_proba(X)

# Tạo DataFrame hiển thị kết quả
result = pd.DataFrame({
    "Buy thực tế": y,
    "P(Buy=No)": probs[:, 0],
    "P(Buy=Yes)": probs[:, 1],
    "Dự đoán": label_y.inverse_transform(model.predict(X))
})

print("📊 Kết quả dự đoán:")
print(result)

# --- Dự đoán cho một mẫu mới ---
new_sample = pd.DataFrame({
    "Age": ["Old"],
    "Income": ["Medium"],
    "Student": ["Yes"],
    "Credit": ["Fair"]
})

# Mã hóa mẫu mới
for col in new_sample.columns:
    new_sample[col] = encoders[col].transform(new_sample[col])

# Tính xác suất
new_prob = model.predict_proba(new_sample)[0]
print("\n🎯 Mẫu mới:", new_sample)
print("P(Buy=No) =", new_prob[0])
print("P(Buy=Yes) =", new_prob[1])
print("→ Dự đoán:", label_y.inverse_transform(model.predict(new_sample))[0])
