import pandas as pd
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Normalizer,LabelEncoder

df = pd.read_csv("glass.csv")
X = df.drop('Type',axis = 1)
y =df["Type"]

minmax_scaler = MinMaxScaler()
X_minmax = pd.DataFrame(minmax_scaler.fit_transform(X),columns=X.columns)
X_minmax['Type'] = y


std_scaler = StandardScaler()
X_std = pd.DataFrame(std_scaler.fit_transform(X),columns=X.columns)
X_std['Type'] = y

normalizer = Normalizer()
X_norm = pd.DataFrame(normalizer.fit_transform(X),columns=X.columns)
X_norm['Type'] = y

zscore_scaler = StandardScaler()
X_zscore = pd.DataFrame(zscore_scaler.fit_transform(X),columns=X.columns)
X_zscore['Type'] = y

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)
df.encoded = df.copy()
df_encoded['Type'] = y_encoded

df.to_csv("glass_original.csv", index=False)
X_minmax.to_csv("glass_minmax.csv", index=False)
X_std.to_csv("glass_standardize.csv", index=False)
X_norm.to_csv("glass_normalize.csv", index=False)
X_zscore.to_csv("glass_zscore.csv", index=False)
df_encoded.to_csv("glass_encoded.csv", index=False)





