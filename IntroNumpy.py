import numpy as np

ventas1 = np.array([100,250,300])
ventas2 = np.array([120,200,350])

ventas_totales = ventas1 + ventas2
ventas_altas = ventas_totales < 400

print(ventas_totales)
print(ventas_altas)

print("\n")

# Sintaxis: np.where(condicion, valor_si_verdadero, valor_si_falso)
edades = np.array([18, 13, 15])
calificacion = np.where(edades >=18, 'adulto', 'menor')

print(edades)
print(calificacion)