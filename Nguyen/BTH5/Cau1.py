import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, LabelEncoder

file_path = 'glass.csv'
df = pd.read_csv(file_path)

df_numeric = df.select_dtypes(include=[np.number])

scaler = MinMaxScaler()
df_min_max = pd.DataFrame(scaler.fit_transform(df_numeric), columns=df_numeric.columns)
# df_min_max.to_csv('glass_min_max_scaled.csv', index=False)

scaler = StandardScaler()
df_standardized = pd.DataFrame(scaler.fit_transform(df_numeric), columns=df_numeric.columns)
# df_standardized.to_csv('glass_standardized.csv', index=False)

scaler = Normalizer()
df_normalized = pd.DataFrame(scaler.fit_transform(df_numeric), columns=df_numeric.columns)
# df_normalized.to_csv('glass_normalized.csv', index=False)

label_encoder = LabelEncoder()
df['Type'] = label_encoder.fit_transform(df['Type'])
# df.to_csv('glass_label_encoded.csv', index=False)
