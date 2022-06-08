
import pandas as pd

lista1 = []
alunos1 = {}
alunos1["ID"] = 3333
alunos1["Telefone"] = 5541998264344
alunos1["Data"] = "Publicado em: Quarta-feira, 25 de Maio de 2022 23h39min03s BRT"
lista1.append(alunos1)
df1 = pd.DataFrame(lista1)

#df=pd.read_csv("user_test.csv", sep=";", index_col=["Telefone"])
lista2 = []
alunos2 = {}
alunos2["ID"] = 6666
alunos2["Telefone"] = 5541998264344
alunos2["Data"] = "Publicado em: Quarta-feira, 25 de Maio de 2022 23h39min03s BRT"
lista2.append(alunos2)
df2 = pd.DataFrame(lista2)
df3=df1.append(df2)
df3.to_csv("TESTE.csv", sep=";", index=False)
print(df3)