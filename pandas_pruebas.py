import pandas as pd

datos = {
    "nombres":["Maria", "Luis", "Carmen"],
    "materias":["Matematicas", "Programacion", "Mercadotecnia"],
    "promedios":[80, 100, 90]
}

df_alumnos = pd.DataFrame(datos)
print(df_alumnos)

df_colesterol = pd.read_csv("https://raw.githubusercontent.com/asalber/manual-python/master/datos/colesteroles.csv")
"""
#print(df_colesterol)
print(df_colesterol.head())
print(df_colesterol.describe())
print(df_colesterol.info())

print(df_colesterol.shape)
print(df_colesterol.size)
print(df_colesterol.columns)
print(df_colesterol.dtypes)
print(df_colesterol.index)
"""

print("fin")