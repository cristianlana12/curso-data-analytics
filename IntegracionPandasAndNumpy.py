import pandas as pd
import numpy as np

df_ventas = pd.DataFrame({
    'precio': [100.5, 200.0, 150.75],
    'cantidad': [2, 5, 1]
})

##Extramos una fila como un arreglo puro de numpy
arreglo_precios = df_ventas['precio'].to_numpy()

print(arreglo_precios)
print(type(arreglo_precios))

'''
to_numpy() convierte la serie de pandas a un ndarray de numpy, la serie debemos elegirla del dataframe
'''

# Matematicas Vectorizadas

# Escenario: Tenemos una columna de ingresos muy asimétrica (skewed)
# y necesitamos aplicarle el logaritmo natural para un modelo de Machine Learning.


df = pd.DataFrame({
    'ingresos': [1000, 50000, 2000000, 1500]
    })

df['log_ingresos_rapdios'] = np.log(df['ingresos'])
# NumPy es lo suficientemente inteligente para recibir una Serie de Pandas, 
# operar en C, y devolver una Serie de Pandas intacta.

print("\n")
print(df)

##A. Condición Simple (np.where)
##Equivalente a IF(condicion, verdadero, falso).

df['estado_meta'] = np.where(df['ingresos'] > 10000, 'supera', 'no supera')
print("\n")
print(df)

print("\n")

##B. Múltiples Condiciones (np.select)

##definimos filtro logico

condicion = [
    (df['ingresos'] <5000),
    (df['ingresos'] >= 5000) & (df['ingresos'] <= 50000),
    (df['ingresos'] > 50000)
]

# Definimos los resultados para cada condición
resultado = ["bajo", "medio", "alto"]

# np.select(condlist, choicelist, default)

df['nivel_ingreso'] = np.select(condicion, resultado, default='sin valor')
print(df)
print("\n")

##4. Gestión del Infinito y Errores Matemáticos
df_errores = pd.DataFrame({
    'ganancia': [100, 200, 0],
    'inversion': [10, 0, 0]
    })
# Esto genera infinitos o NaN (división por cero)
df_errores['ROI'] = df_errores['ganancia'] / df_errores['inversion']
print(df_errores)

'''
   ganancia  inversion   ROI
0       100         10  10.0
1       200          0   inf
2         0          0   NaN

'''

df_errores['ROI'] = df_errores['ROI'].replace([np.inf, -np.inf], np.nan)
df_errores['ROI'] = df_errores['ROI'].fillna(0) # Regla de negocio: ROI 0 si no hubo inversión
print(df_errores)
'''
   ganancia  inversion   ROI
0       100         10  10.0
1       200          0   0.0
2         0          0   0.0
'''















