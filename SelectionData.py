import pandas as pd

data = {
    "Nombre" : ["Ana", "Juan", "Pedro", "Maria", "Luis"],
    "Edad": [22,25,28,23,20],
    "Ciudad": ["Barcelona", "Madrid", "Valencia", "Sevilla", "Bilboa"]
}

df = pd.DataFrame(data=data)

print(df)

##Seleccion por columna

print("\nSeleccion por columna [Edad]")
edades = df["Edad"]
print(edades)

##Seleccion de varias columnas
print("\nSeleccion de varias columnas")
print(df[["Nombre","Ciudad"]])

##Seleccion por indice
print("\nFiltrado por indice")
fila = df.loc[2];
print(fila)


##Seleccion por condicion
print("\nSeleccion por condicion")
personasMayores18 = df[df["Edad"] >= 25]
print(personasMayores18)


##Seleccion por condoncion compuest
print("\nSelecccion por condicion compuesta")
filtro = (df["Edad"] > 23) | (df["Nombre"].str.startswith("A"))
print(df[filtro])

##Seleccion por query
print("\nSeleccion por query")
print(df.query("Edad > 23"))
