import pandas as pd

df = pd.read_csv("./exemplo.csv")

df_filtrado = df[df["estado"] == "SP"]

df_filtrado = df[df["preco"] == "10,50"]

print(df_filtrado)


df2 = pd.read_csv("./exemplo2.csv")

df_filtrado2 = df2[df2["estado"] == "DF"]

df_filtrado2 = df2[df2["preco"] == "10,50"]

print(df_filtrado2)
