import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##ejemplo grafica sencilla

x = [0,1,2,3,4,5]
y = [0,1,4,9,16,25]

plt.plot(x,y) ##genera la grafica
plt.scatter(x,y) ##muestra cada punto
plt.xlabel("eje x") ##da nombre a los ejes
plt.ylabel("eje y") 
plt.title("grafica") ##da titulo a la grafica
plt.show() ##muestra la grafica



