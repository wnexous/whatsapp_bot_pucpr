caractere_identificacao = "#"
nome_evento = ''
import pandas as pd
adicionar_evento = []
pd.DataFrame(adicionar_evento, columns=['Data', "Hora", "Descricao"])

#print(pd.DataFrame(df, columns=['Data', "Hora", "Descricao"]))

df = pd.read_csv('eventos.csv',  sep=';')

def administradores(adm_usr):
    adm = pd.read_csv('Administrador.csv',  sep=';')
    for x in adm['Administrador']:
        if x in adm_usr:
            return(True)
        else:
            False
            
loop_add_evento = 0
while True:
    try:
        data_evento = df["Data"][loop_add_evento]
        hora_evento = df["Hora"][loop_add_evento]
        descricao_evento = df["Descricao"][loop_add_evento]
        adicionar_evento.append([data_evento, hora_evento, descricao_evento])
        loop_add_evento = loop_add_evento + 1
    except Exception:
        break
    
df = pd.DataFrame(adicionar_evento, columns=['Data', "Hora", "Descricao"])
df.to_csv('eventos.csv', sep=';', index_label=["Indice"])





while True:
    evento = input('entrada: ')
    evento = evento.replace(caractere_identificacao, '')
    reconhecimento = evento.strip()
    if reconhecimento[:6] == 'evento':
        evento = evento.replace('evento', '')
        evento = evento.replace('evento ', '')
        
        reconhecimento_evento = evento.split()
        evento = ""
        try:
            if reconhecimento_evento[0] == 'add':
                del reconhecimento_evento[0]
                desc_final = ""
                data_posto = False
                hora_posto = False
                descricao = reconhecimento_evento
                for x in reconhecimento_evento:
                    x = x.replace("desc:", "")
                    if x.count("data:") == 1:
                        data_evento = x.replace("data:", "")
                        data_posto = True
                    else:
                        if  x.count("dia:") == 1:
                            data_evento = x.replace("dia:", "")
                            data_posto = True
                        else: 
                            if x.count("hora:") == 1:
                                hora_evento = x.replace("hora:", "")
                                hora_posto = True
                            else:
                                desc_final = desc_final + x + " "
                if data_posto and hora_posto:
                    adicionar_evento.append([data_evento, hora_evento, desc_final])
                    
                    df = pd.DataFrame(adicionar_evento, columns=['Data', "Hora", "Descricao"])
                    df.to_csv('eventos.csv', sep=';', index_label=["Indice"])
                    df = pd.read_csv('eventos.csv', sep=';')
                else:
                    evento = """
*Parametros nao foram encontrados!*
lista de parametros faltantes:
"""
                    if not data_posto:
                        evento = evento + """
data nao encontrada!. tente adicionar data:dia/mes
                        """
                    if not hora_posto:
                        evento = evento + """
hora nao encontrada!. tente adicionar hora:hora_do_evento
"""
            if reconhecimento_evento[0] == 'rm':

                del reconhecimento_evento[0]
                for indice_remove in reconhecimento_evento:
                    try:
                        df = df.drop(int(indice_remove))
                        df = pd.DataFrame(df, columns=['Data', "Hora", "Descricao"])
                        df.to_csv('eventos.csv', sep=';', index_label=["Indice"])
                    except Exception:
                        evento = ('Nao foi possivel deletar o evento de numero:', indice_remove)
            if reconhecimento_evento[0] == 'list':
                list_df = pd.read_csv('eventos.csv', sep=';')
                evento = list_df.to_string(index=False)
        except Exception:
            evento = f"""
Aqui eh a area do eventos :)

Tente:
*Ver list de eventos:*
{caractere_identificacao}evento ver

*Adicionar evento:*
{caractere_identificacao}evento add dia:dia/mes hora:hora descricao_sobre_o_evento
Ex: {caractere_identificacao}evento add dia:10/05 hora:10 prova de programacao

*Remover evento:*
{caractere_identificacao}evento rm nome
Ex: {caractere_identificacao}evento rm festa da batata
"""
        print(str(evento))