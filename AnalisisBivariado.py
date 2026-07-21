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
analisis bivariado:
    se centra en estudiar las relaciones entre 2 variables, podemos usar graficos de dispercio, de barras
    
    total de cuenta vs propina
'''
sns.scatterplot(data=df, x ="total_bill", y = "tip")
plt.show()

sns.barplot(data=df, x="sex", y= "tip")
plt.show()

sns.boxplot(data=df, x="sex", y='total_bill')
plt.show()