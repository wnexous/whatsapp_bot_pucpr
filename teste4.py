from dataclasses import replace
from time import strftime; import pandas as pd; from datetime import date, datetime
usuario_atual = []
#rd = pd.read_csv("usuarios.csv", sep=';')
#for x in zip(rd["Telefone"].replace("+", "").replace("-", "").replace(" ", ""), rd["Apelido"], rd["Notificacao"], rd["Materias"], rd["Ultimo Aviso DATA"], rd["Data de envio"], rd["Hora de envio"], rd["Menu"]):  usuario_atual.append(x)
notificacao = "s"; ultimo_aviso = ""; apelido_usuario = "feijao"; telefone = input("Telefone: ").replace("+", "").replace("-", "").replace(" ", ""); materias=""; menu="hub"
data_envio = datetime.today().strftime("%d/%m/%Y"); hora_envio = datetime.today().strftime("%H:%M:%S")
usuario_atual.append([telefone, apelido_usuario, notificacao, materias, ultimo_aviso, data_envio, hora_envio, menu])
try:    pd.DataFrame(usuario_atual, columns=["Telefone", "Apelido", "Notificacao", "Materias","Ultimo Aviso DATA", "Data de envio", "Hora de envio", "Menu"]).to_csv("usuarios.csv", sep=";", index=False)
except Exception:   print("Excel aberto")