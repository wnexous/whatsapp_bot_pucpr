from dataclasses import replace
from time import strftime; import pandas as pd; from datetime import date, datetime
def nome_grupo():   return "+55 41 96807768"
evento="materia remove 3331 3333"
evento=evento.replace("materia remove ", "")
nome_usuario =  int(nome_grupo().replace("+", "").replace("-", "").replace(" ", ""))
for x in pd.read_csv("usuarios.csv", sep=';',index_col=["Telefone"]).loc[[nome_usuario]]["Materias"]:
  materia_a_remover = (str(x))
not_find=''
for y in evento.split():
  if y in materia_a_remover:
    materia_a_remover=materia_a_remover.replace(y, "").replace("  ", "")
  else: 
    not_find = not_find+" "+y  
    evento=f"oopa, nao encontrei a materia{not_find} na sua lista de materias"
#evento=saida

try:
  new_list = []
  rd = pd.read_csv("usuarios.csv", sep=';')
  for y in zip(rd["Telefone"], rd["Apelido"], rd["Notificacao"], rd["Materias"], rd["Ultimo Aviso DATA"], rd["Data de envio"], rd["Hora de envio"], rd["Menu"]):
    if (y[3]=="nan" or y[3] =="" or y[3] ==" " or materia_a_remover=="nan"):
      pass
    else:
      if y[0] == nome_usuario:
        new_list_two = {}
        new_list_two["Telefone"] = y[0]
        new_list_two["Apelido"] = y[1]
        new_list_two["Notificacao"] = y[2]
        new_list_two["Materias"] = str(materia_a_remover).replace(",", "").replace("[", "").replace("]", "").replace("'", "").replace("nan ", " ").replace("nan", "").replace("  ", " ").replace(".0", "")
        new_list_two["Ultimo Aviso DATA"] = y[4]
        new_list_two["Data de envio"] = y[5]
        new_list_two["Hora de envio"] = datetime.today().strftime("%H:%M:%S")
        new_list_two["Menu"] = y[7]
        new_list.append(new_list_two)
        if materia_a_remover == " "or materia_a_remover=="":
          evento="atualmente voce nao tem zero materias para receber notificacao pois todas foram removidas"
        else:
          evento=f"materia {materia_a_remover} removidas com sucesso"
        
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
      if (y[3]=="nan" or y[3] =="" or y[3] ==" " or materia_a_remover=="nan"):
          evento="atualmente voce nao tem zero materias para receber notificacao"
      pd.DataFrame(new_list).to_csv("usuarios.csv", sep=";", index=False)
except Exception: evento=="opa amg, deu um erro aqui no role, tenta falar com o nexus pra ele dar um jeito. nome do erro: rmlstontry"
#rmlstontry
print(evento)