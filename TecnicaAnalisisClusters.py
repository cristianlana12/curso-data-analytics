import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans


df = sns.load_dataset("iris")

models = KMeans(n_clusters=3, random_state=42)  ##3 categorias de flores
df["cluster"] = models.fit_predict(df.iloc[:,:-2])
print(df)


sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="cluster")
plt.show()