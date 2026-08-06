import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

'''
Ocupamos PCA para dataset con muchas dimensiones
'''

df = sns.load_dataset("iris")
print(df)
df.iloc[:,:-1]

pca_model = PCA(n_components=2)
df_pca = pca_model.fit_transform(df.iloc[:,:-1])
print(df_pca)


plt.scatter(df_pca[:,0], df_pca[:,1],c=df["species"].astype("category").cat.codes)
plt.xlabel("PCA1")
plt.ylabel("PCA2")
plt.show()