import pandas as pd

numeros = [3,4,5,7,8]

##CREAMOS UNA SERIE
serie = pd.Series(numeros)
print(serie)
print(type(serie))


##Para crear un DataFrame debemos usar un dict
data = {
    "nombre": ["cristian", "fernando", "nancy"],
    "edad": [23,23,12]
}

print(data)
print(type(data))

##creamos el DataFrame
df = pd.DataFrame(data=data)
print(df)

df.to_parquet("datosEmpleados.parquet")


import_df = pd.read_parquet("datosEmpleados.parquet")
import_df.info()