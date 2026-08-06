import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = sns.load_dataset("iris")

std_scaler = StandardScaler()
df_std_scaler = std_scaler.fit_transform(df.iloc[:,:-1])
print(df_std_scaler)

mm_scaler = MinMaxScaler()
df_normalized = mm_scaler.fit_transform(df.iloc[:,:-1])
print(df_normalized)