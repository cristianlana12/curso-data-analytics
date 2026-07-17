import pandas as pd

# 1. Tabla Izquierda (Transaccional)
ventas = pd.DataFrame({
    'id_venta': [101, 102, 103],
    'id_cliente': ['C1', 'C2', 'C99'], # Ojo: C99 no existe en la tabla clientes
    'total': [1500, 2300, 900]
})

# 2. Tabla Derecha (Catálogo/Dimensional)
clientes = pd.DataFrame({
    'id_cliente': ['C1', 'C2', 'C3'], # C3 no compró nada
    'nombre': ['Ana', 'Juan', 'Pedro'],
    'ciudad': ['Madrid', 'Barcelona', 'Valencia']
})

## left join

df_final = pd.merge(
    left=ventas,
    right=clientes,
    on='id_cliente',  ##fk usada como referenciador
    how='left',  ##left join nos quedamos con la tabla de la izquierda y las coincidencias entre izq y der
    validate= 'm:1' ##Exigimos: Muchas ventas (m) por cada 1 cliente único
)

print(df_final)

''' 
hace la inteccion, y nos quedamos con los datos puros de ventas como tal, al c3 no coincidir con los id_clientes de venta no lo agrega 
completa con NaN los datos faltantes de la venta de c99

      id_venta  id_cliente  total  nombre     ciudad
0       101         C1      1500    Ana       Madrid
1       102         C2      2300    Juan     Barcelona
2       103        C99      900     NaN        NaN

si usabamos inner, o sea coincidencias unicamente, la venta 103 se hubiera perdido
'''


'''
Si hacemos un merge mal en un entorno de millones de datos, podemos causar un producto cartesiano, multiplicando la cantidad de filas
y colapsando la memoria del servidor, puesto que panda corre todo en memoria 
Para cubrirnos de esto usaremos el parametro VALIDATE   
Si por error tu tabla de clientes tiene a "Ana" duplicada, el merge va a duplicar todas las ventas de Ana silenciosamente, arruinando tu reporte financiero.
'''