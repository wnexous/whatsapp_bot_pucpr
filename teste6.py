import pandas as pd
df=pd.read_csv("usuarios.csv", sep=";", index_col=["Telefone"])
df = df.loc[554198264344]["Menu"]
print(df)