import pandas as pd
data ={
    "Nombre": ["Ana", "Juan", "Pedro", "Maria", "Luis", "Carlos", "Sofia"],
    "Edad": [22, 25, 28, 23, 20, 35, 22],
    "Ciudad": ["Madrid", "Madrid", "Valencia", "Madrid", "Bilbao", "Valencia", "Bilbao"],
    "Salario": [2000, 2500, 3000, 2200, 1800, 4000, 1900]
}

df = pd.DataFrame(data=data)

##¿Cuál es el salario promedio en cada ciudad?"
print("Salario por ciudad")
salario_promedio = df.groupby("Ciudad")["Salario"].mean()
print(salario_promedio)

print("\n")

##Múltiples Métricas a la Vez
## usamos la función .agg() (Aggregate).
print("Múltiples Métricas a la Vez")

resumen_ciudades = df.groupby("Ciudad").agg(
    salario_promedio = ("Salario", "mean"),
    Edad_maxima = ("Edad", "max"),
    Cantidad_empleados = ("Nombre", "count")
).reset_index()

print(resumen_ciudades)

'''
reset_index() sirve para que la tabla vuelva a tener estructura plana y tradicional
porque al querer importar estos datos con metricas multiples tendremos el problema
que tendran como indice la tabla por la cual agrupas, en este caso, "Ciudad" y en
parquet o powerby o otros, necesimos indices numericos
'''
