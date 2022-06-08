
import pandas as pd
nome_usuario = 554198264344
evento = "3334 farinha"


df=pd.read_csv("data_user.csv", sep=";")

if df.loc[(df['Materias'] == 6666) & (df['Telefone'] == nome_usuario)].bool:
    print("sim")
else:
    print("nao")

df = df.drop(df[(df['Materias'] == 1234) & (df['Telefone'] == nome_usuario)].index)
#df.to_csv("data_user.csv", sep=";", index=False)
print(df)