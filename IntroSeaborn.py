import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

##ejemplo grafica de dispercion

'''
searborn tiene data set cargados que podemos usar
en este caso cargamos el iris que es un dataset de flores, que nos da medidas de setas y petalos en largo y ancho
'''

data = sns.load_dataset("iris")
print(data)

##instanciamos el sns

graficaSns = sns.scatterplot(x="sepal_length", y = "sepal_width", hue="species", data=data)
plt.xlabel = "longitud setas"
plt.ylabel = "ancho setas"
plt.title = "Gafico dispercion"
plt.show()

##grafica de ridgeplot
##esta grafica nos permite observar las distribuciones de cada medidas

setosa = data[data["species"] == "setosa"]
versicolor = data[data["species"] == "versicolor"]
virginica = data[data["species"] == "virginica"]

##configuramos la figura y los ejes 8 x 6 pulgadas
fig, ax = plt.subplots(figsize = (8,6))
plt.xlabel = "longitud del petalo"
plt.ylabel = "observaciones del petalo"

#usamos la funcion kdeplot
sns.kdeplot(data= setosa["petal_length"], label = "setosa", ax=ax, fill=True)
sns.kdeplot(data= versicolor["petal_length"], label = "versicolor", ax=ax, fill=True)
sns.kdeplot(data= virginica["petal_length"], label = "virginica", ax=ax, fill=True)

##ajustamos la posicion de las leyendas
ax.legend(loc="upper right")

plt.title= 'Ridge plot - data set iris'
plt.show()

