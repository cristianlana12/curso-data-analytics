import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style(style="darkgrid")
df = sns.load_dataset("tips")

print(df)

##barra de promedio de propinas por sexo
sns.barplot(data=df, x="sex", y = "tip", errorbar=None)
plt.title("Propinas promedio por sexo")
plt.show()

##barra de promedio de propina por dia
sns.barplot(data=df, x= "day", y = "tip", errorbar=None)
plt.title("Propinas promedio por dia")
plt.show()