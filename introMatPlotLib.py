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



##graficas de barra

categorias = ['A', 'B', 'C', 'D', 'E']
valores = [10,20,25,40,60]

plt.bar(categorias,valores)
plt.show()


edades = [20, 25, 30, 35]
salarios = [1500, 2000, 2500, 3200]
# fig = La ventana completa (el lienzo)
# ax = El gráfico específico dentro de la ventana
fig, ax = plt.subplots(figsize=(10, 6)) # Definimos el tamaño en pulgadas

# Operamos directamente sobre el objeto 'ax'
ax.plot(edades, salarios, color='blue', marker='o', linestyle='--')

# La nomenclatura cambia: usamos set_...
ax.set_title("Evolución Salarial por Edad", fontsize=14, fontweight='bold')
ax.set_xlabel("Edad del Empleado")
ax.set_ylabel("Salario (USD)")

# Limpieza visual (Quitar bordes innecesarios)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()