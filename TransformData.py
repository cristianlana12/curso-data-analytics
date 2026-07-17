import pandas as pd
import numpy as np

data = {
    "Nombre" : ["Ana", "Juan", "Pedro", "Maria", "Luis"],
    "Edad": [22,25,np.nan,23,20],
    "Ciudad": ["Barcelona", "Madrid", "Valencia", None, "Bilboa"]
}

df = pd.DataFrame(data=data)

##diagnostico general, veremos todo el df para saber que datos faltan
print(df)

##tratamiento de nulos/*

print("\n\n")
##media_edad = df["Edad"].median
##df["Edad"] =df["Edad"].fillna(media_edad)
##print(df)
print("cantidad de nulos_: ")
print(df.isna().sum())
print("\n")

df_fill = df.fillna(
    {
        'Edad' : df["Edad"].mean(),
        'Ciudad' : 'Desconocido'
    }
)
##volvemos los valores de edad a INT

df_fill["Edad"] = df_fill["Edad"].round().astype(int)

print(df_fill)