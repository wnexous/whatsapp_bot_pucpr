
import pandas as pd
nome_usuario = 5541998264376
evento = "3334 farinha"

df=pd.read_csv("data_user.csv", sep=";")
saida=''
for materia_por_evento in evento.split():
    if materia_por_evento.isnumeric():
        try:
            for x in pd.read_csv("curso_lista.csv", sep=";", index_col=["ID"]).loc[[int(materia_por_evento)]]["Materia"]:  nome_da_materia=x
            try:    pd.read_csv("data_user.csv", sep=";", index_col=["Materias"]).loc[[int(materia_por_evento)]];saida+=f"\n{nome_da_materia}ja esta adicionada na sua lista de materias"
            except Exception:   
                try:
                    aluno_new = {"Telefone":[str(nome_usuario)],"Materias":[materia_por_evento],"Notificacao":["-"]}
                    df_newuser=pd.DataFrame(aluno_new)
                    df=pd.concat([df, df_newuser])
                    saida+=f"\n{nome_da_materia}foi adicionada com sucesso!"
                except Exception:   saida+=f"\n{materia_por_evento} nao existe em nossa lista de cursos disponiveis."
        except Exception:   saida+=f"\n{materia_por_evento} nao existe em nossa lista de cursos disponiveis"
    else:   saida+=f"\n{materia_por_evento} não é um ID! consulte o menu de materia para saber o ID"
df.to_csv("data_user.csv", sep=";", index=False)
evento=saida


print(evento)