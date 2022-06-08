from dataclasses import replace
from time import strftime; import pandas as pd; from datetime import date, datetime

def nome_grupo():   return "+55 41 96807768"
evento="materia adicionar 3333"
nome_usuario =  int(nome_grupo().replace("+", "").replace("-", "").replace(" ", ""))
confirmacao = True
for y in pd.read_csv("usuarios.csv", sep=';',index_col=["Telefone"]).loc[[nome_usuario]]["Materias"]:
    for x in evento.split():
        try:
            if x in y:
                confirmacao = False
                evento=f"calma ai manito, parece q a materia {x} ja esta adicionada."
        except Exception: pass
if confirmacao:
    try:
        nome_usuario =  int(nome_grupo().replace("+", "").replace("-", "").replace(" ", ""))
        materia_a_adicionar=[]
        for x in pd.read_csv("usuarios.csv", sep=';',index_col=["Telefone"]).loc[[nome_usuario]]["Materias"]: materia_a_adicionar.append(x)
        for x in evento.split():
            if x.isnumeric():
                try:
                    for z in pd.read_csv("curso_lista.csv", sep=';',index_col=["ID"]).loc[[int(x)]]["Materia"]:

                        if not materia_a_adicionar.count(int(x)) >=1:   materia_a_adicionar.append(x);evento="Materia(s) adicionada(s) com sucesso."
                        else:   evento-f"{x} ja adicionado"

                        
                except Exception:   evento=f"Estranho mano, parece que a materia {x} nao existe."
    except Exception:
        evento = "Que estranho, nao estou conseguindo identificar seu numero de telefone. Tenta falar com o Nexus pra ver se ele manja de arrumar"
        print(evento)
        
    new_list = []
    rd = pd.read_csv("usuarios.csv", sep=';')
    for y in zip(rd["Telefone"], rd["Apelido"], rd["Notificacao"], rd["Materias"], rd["Ultimo Aviso DATA"], rd["Data de envio"], rd["Hora de envio"], rd["Menu"]):
        if y[0] == nome_usuario:
            new_list_two = {}
            new_list_two["Telefone"] = y[0]
            new_list_two["Apelido"] = y[1]
            new_list_two["Notificacao"] = y[2]
            new_list_two["Materias"] = str(materia_a_adicionar).replace(",", "").replace("[", "").replace("]", "").replace("'", "").replace("nan ", "").replace(".0", "").replace("  ", "")
            new_list_two["Ultimo Aviso DATA"] = y[4]
            new_list_two["Data de envio"] = y[5]
            new_list_two["Hora de envio"] = datetime.today().strftime("%H:%M:%S")
            new_list_two["Menu"] = y[7]
            new_list.append(new_list_two)
            #evento=evento+f" Novas materias: {str(materia_a_adicionar)}"
        else:
            new_list_two = {}
            new_list_two["Telefone"] = y[0]
            new_list_two["Apelido"] = y[1]
            new_list_two["Notificacao"] = y[2]
            new_list_two["Materias"] = y[3]
            new_list_two["Ultimo Aviso DATA"] = y[4]
            new_list_two["Data de envio"] = y[5]
            new_list_two["Hora de envio"] = y[6]
            new_list_two["Menu"] = y[7]
            new_list.append(new_list_two)
    try:    pd.DataFrame(new_list).to_csv("usuarios.csv", sep=";", index=False)
    except Exception:   pass

if "materia adicionar" in evento:
    evento='eii, vc precisa colocar o id da materia\ntipo ex: "materia adicionar 3333".\nTambem nao se esqueca da hashtag no inicio do comando'
print(evento)