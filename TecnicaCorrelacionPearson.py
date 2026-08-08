import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr

df = sns.load_dataset("iris")


#Calculamos la correlacion de pearsonr

correlacion, _ = pearsonr(df["sepal_length"],df["petal_length"])

print(f"la correlacion entre sepal y petal length es: {correlacion}")  #la correlacion entre sepal y petal length es: 0.8717537758865831

## al ser <1 