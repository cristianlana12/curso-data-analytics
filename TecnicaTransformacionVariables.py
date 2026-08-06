import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset("iris")
sns.displot(data=df, x = 'sepal_length', hue="species", kde=True)

##transformacion logaritmica

df["sepal_length_log"] = np.log(df["sepal_length"])
sns.displot(data=df, x = 'sepal_length_log', hue="species", kde=True)
plt.show()