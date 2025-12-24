import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, LabelEncoder
from scipy.fft import fft
from scipy.fftpack import dct

df = pd.read_csv(r'C:\Users\van46\PycharmProjects\FeXam\sample_dataset.csv')

#a. min max scaler
# scaler_minmax = MinMaxScaler(feature_range=(1, 5)) dua ve doan (1, 5)
scaler_minmax = MinMaxScaler()
df['feature_1'] = scaler_minmax.fit_transform(df[['feature_1']])

#b. Standardalize Data cho cot 2
scaler_std = StandardScaler()
df['feature_2'] = scaler_std.fit_transform(df[['feature_2']])

#c.Normalize Data cho cot 3
scaler_norm = Normalizer()
df['feature_3'] = scaler_norm.fit_transform(df[['feature_3']].values.T).T

#d. Thuc hien Fourier Transform
fft.values = fft(df['feature_1'].values)
print("Ket qua fourier transform tren cot 1: \n", fft.values)

#e. So hoa cot cuoi cung
le = LabelEncoder()
df['class'] = le.fit_transform(df['class'])

# result = df.to_csv('sample_datasetAfter.csv', index=False)
print("\nBang du lieu sau khi xu ly: ")
print(df)

print("-" * 60)

#d. Thuc hien DCT tren bo du lieu (Vi du cot 1)
data_dct = dct(df['feature_1'].values, norm='ortho')

#e. So hoa cot cuoi cung
leA = LabelEncoder()
df['class'] = leA.fit_transform(df['class'])
print("\nBang du lieu sau khi xu ly: ")
print(df)




