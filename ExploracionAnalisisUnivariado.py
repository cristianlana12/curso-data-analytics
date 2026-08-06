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

df = sns.load_dataset("tips")  ##datos que estan cargados de propinas de un bar, con datos
print(df)

'''
    Siempre que llega un dataset identificamos que variables queremos predecir
    hacemos un pequeño analisis primario para obtener info del data set
'''
print("\ninfo de df: ")
df.info()

print("\ndescripcion:")
print(df.describe())

'''
    primera seccion de analisis univariado:
        implica examinar una variable a la vez, usando histogramas, diagramas de caja, graficos de densidad
        esto nos da info de como varia una variable y analisar su comportamiento
'''
sns.histplot(data=df, x="total_bill")
plt.plot()
plt.show()

sns.boxplot(data=df, x="total_bill")
plt.plot()
plt.show()

sns.kdeplot(data=df, x="total_bill")
plt.plot()
plt.show()

