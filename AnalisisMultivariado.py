import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
El analisis de datos explotaratorios es una tecnica aplicada en estadistica y ciencias de datos
con el objetivo de resumir, visualizar y analisis un conjunto de datos, para extraer patrones y tendencias

sumamente importante para comprender los datos antes de usar modelos predictivos 
'''

sns.set_style("darkgrid")
df = sns.load_dataset("tips")

'''
El analisis multivariado implica analisis mas de 2 variables al mismo tiempo
usar graficos de dispercion en pares, otros
'''

sns.pairplot(df, hue="sex")  ##comparacion con todas las variables numericas entre los sexos
plt.show()