import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)  #establecer semilla de nro aleatorios
##generamos datos ejemplos
edad_autos = np.random.randint(0,20,size=200)
precio_auto = 30 - edad_autos + np.random.normal(-3,3, size=200)

data = pd.DataFrame({
    "edad" : edad_autos,
    "precio" : precio_auto
})

print(data)

##creacion de grafico
fig, ax = plt.subplots(2,2, figsize = (12,10))

##grafico de dispercion de edad
ax[0,0].scatter(data["edad"], data["precio"], alpha=0.5)
ax[0,0].set_xlabel("edad automobil")
ax[0,0].set_ylabel("precio")
ax[0,0].set_title("edad vs precio")


##histograma de edad

sns.histplot(data["edad"], ax = ax[0,1], kde=True, color="g")
ax[0,1].set_xlabel("edad automobil")
ax[0,1].set_ylabel("frecuencia")
ax[0,1].set_title("histograma edad")


##histograma de precio
sns.histplot(data["precio"], ax= ax[1,0], kde=True, color='r')
ax[1,0].set_xlabel("precio automobil")
ax[1,0].set_ylabel("frecuencia")
ax[1,0].set_title("histograma precio")

##eliminamos 4to subplot ax[1,1]
ax[1,1].axis("off")

plt.subplots_adjust(wspace=0.3, hspace=0.3)

plt.show()
