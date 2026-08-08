import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df = sns.load_dataset("iris")

#Calculamos el Z-score
df["z-score_sepal_length"] = np.abs((df["sepal_length"] - df["sepal_length"].mean()) / df["sepal_length"].std())
print(df)

outliers = df[df["z-score_sepal_length"] > 2]
print(outliers)

sns.scatterplot(data=df, x="sepal_length", y="petal_length", hue="species")

sns.scatterplot(data=outliers, x="sepal_length", y="petal_length", c="red")
plt.show()