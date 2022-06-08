from time import strftime
from numpy import NaN; import pandas as pd; from datetime import date, datetime
import time
import unidecode
try:
    def todas_materias(evento):
        def mat_list():
            saida_mat = []
            for x in pd.read_csv('curso_lista.csv',  sep=';')["Materia"]:  saida_mat.append(x)
            return saida_mat
        def id_list():
            saida_id = []
            for y in pd.read_csv('curso_lista.csv',  sep=';')["ID"]: saida_id.append(y)
            return saida_id
        looping = 0
        a=evento;evento=""
        for y in zip(mat_list(), id_list()):
            try:
                if unidecode.unidecode(a).lower().replace(" ", "") in unidecode.unidecode(y[0]).lower().replace(" ", ""):
                    evento=evento+(f"*ID:* {y[1]}\n*Materia:* {y[0]}\n")
                    
                    looping = looping + 1
                    if looping >=20:
                        evento="*Limite maximo de 20 materias por pesquisa*"+evento
                        break
            except Exception:   
                pass
        return evento
    def criar_conta(evento, telefone):
        try: 
            for y in pd.read_csv("usuarios.csv", sep=';',index_col=["Telefone"]).loc[[int(telefone)]]["Materias"]:
                evento = "Heey, voce ja tem uma conta criada"
        except Exception:
            if len(evento) <= 20:
                usuario_atual = []
                rd = pd.read_csv("usuarios.csv", sep=';')
                for x in zip(rd["Telefone"], rd["Apelido"], rd["Notificacao"], rd["Materias"], rd["Ultimo Aviso DATA"], rd["Data de envio"], rd["Hora de envio"], rd["Menu"]):  usuario_atual.append(x)
                notificacao = "s"; ultimo_aviso = "";apelido_usuario=evento;materias="";menu="hub"
                data_envio = datetime.today().strftime("%d/%m/%Y"); hora_envio = datetime.today().strftime("%H:%M:%S")
                usuario_atual.append([telefone, apelido_usuario, notificacao, materias, ultimo_aviso, data_envio, hora_envio, menu])
                try:    pd.DataFrame(usuario_atual, columns=["Telefone", "Apelido", "Notificacao", "Materias","Ultimo Aviso DATA", "Data de envio", "Hora de envio", "Menu"]).to_csv("usuarios.csv", sep=";", index=False)
                except Exception:   print("Excel aberto")
                evento=f"conta criada com sucesso!\nBem vindo {apelido_usuario}"
            else:   evento="o seu apelido nao pode ter mais do que 20 caracteres"

        return evento
    def administradores(nome_usuario):
        adm = pd.read_csv('Administrador.csv',  sep=';', index_col=['Administrador'])
        
        for x in adm.loc[[nome_usuario]].index:
            try:
                if x == nome_usuario:
                    return True
                else:
                    return False
            except Exception:   pass  
    def adicionar_materia(evento, nome_usuario):
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
        return saida    
            
    def remove_materia(a, nome_grupo):
        evento=a.replace("materia remover ", "")
        evento=a.replace("materia remover", "")
        nome_usuario = int(nome_grupo.replace("+", "").replace("-", "").replace(" ", ""))
        for x in pd.read_csv("usuarios.csv", sep=';',index_col=["Telefone"]).loc[[nome_usuario]]["Materias"]:   materia_a_remover = (str(x))
        not_find=''
        for y in evento.split():
            if y in materia_a_remover:  materia_a_remover=materia_a_remover.replace(y, "").replace("  ", "")
            else: 
                not_find = not_find+" "+y  
                evento=f"oopa, nao encontrei a materia{not_find} na sua lista de materias"
        try:
            new_list = []
            rd = pd.read_csv("usuarios.csv", sep=';')
            for y in zip(rd["Telefone"], rd["Apelido"], rd["Notificacao"], rd["Materias"], rd["Ultimo Aviso DATA"], rd["Data de envio"], rd["Hora de envio"], rd["Menu"]):
                if (y[3]=="nan" or y[3] =="" or y[3] ==" " or materia_a_remover=="nan"):    pass
                else:
                    if y[0] == int(nome_usuario):
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
                        print(new_list)
                        if materia_a_remover == " "or materia_a_remover=="":
                            evento="atualmente voce nao tem zero materias para receber notificacao pois todas foram removidas"
                        else:
                            evento=f"materia(s) removida(s) com sucesso"
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
                    if (y[3]=="nan" or y[3] =="" or y[3] ==" " or materia_a_remover=="nan"):    evento="atualmente voce nao tem zero materias para receber notificacao"
                    pd.DataFrame(new_list).to_csv("usuarios.csv", sep=";", index=False); print(pd.DataFrame(new_list))
        except Exception:
            evento ="opa amg, deu um erro aqui no role, tenta falar com o nexus pra ele dar um jeito. nome do erro: rmlstontry"
        #rmlstontry
        return evento    
    def materia_list(evento, nome_grupo):
        materias_para_escrita=""
        try:
            for x in pd.read_csv("usuarios.csv", sep=';', index_col=["Telefone"])["Materias"].loc[[int(nome_grupo)]]:
                materia=""
                materia+=str(x).replace(".0", "")
                if materia =="nan" or materia =="" or materia ==" ": materias_para_escrita="_nenhuma materia encontrada._"
                else:   
                    for x in materia.split():
                        try:
                            for z in pd.read_csv("curso_lista.csv", sep=';',index_col=["ID"]).loc[[int(x)]]["Materia"]: materias_para_escrita+="*ID:* "+x+"\n"+z+"\n\n"
                        except Exception:   pass
                evento=(f"*Materias atuais:*\n{materias_para_escrita}")
        except Exception:   evento = "ops, parece que voce ainda nao tem uma conta. "
        print(evento)
        return evento
    def delay_loop():   return 1000
    def delay_espera(): return 1
    
    
    #Mensagens
    def change_menu(nome_grupo, menu):
        rd = pd.read_csv("usuarios.csv", sep=';')
        new_list = []
        for p in range(0,20):
            for y in zip(rd["Telefone"], rd["Apelido"], rd["Notificacao"], rd["Materias"], rd["Ultimo Aviso DATA"], rd["Data de envio"], rd["Hora de envio"], rd["Menu"]):
                if y[0] == int(nome_grupo):
                    new_list_two = {}
                    new_list_two["Telefone"] = y[0]
                    new_list_two["Apelido"] = y[1]
                    new_list_two["Notificacao"] = y[2]
                    new_list_two["Materias"] = y[3]
                    new_list_two["Ultimo Aviso DATA"] = y[4]
                    new_list_two["Data de envio"] = y[5]
                    new_list_two["Hora de envio"] = datetime.today().strftime("%H:%M:%S")
                    new_list_two["Menu"] = menu
                    new_list.append(new_list_two)
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
            try:
                pd.DataFrame(new_list).to_csv("usuarios.csv", sep=";", index=False)
                break
            except Exception:   time.sleep(5);evento="ohoh, ocorreu algum bug e nao conseguimos mudar seu menu";return evento
    def msg_hub():
        evento = """
1. Meu perfil
2. Materias

9. Considerações"""
        return evento
    def msg_materia():
        evento="""
9. Voltar ao Hub principal
"""
        return evento
    def msg_materia_menu():
        evento="""
1. Para listar suas materias
2. Para adicionar materia
3. Para remover materia
4. Para procurar uma materia
9. Para retornar ao HUB
"""
        return evento
    def msg_addmateria():
        evento="Para *adicionar* as materias pelo nome, utilize o *id_da_materia*.\n\nEx1.: _3304_\n\nCaso deseje retornar, digite *sair*"
        return evento
    def msg_rmmateria():
        evento="Para *remover* as materias pelo nome, utilize o *id_da_materia*.\n\nEx1.: _3304_\n\nCaso deseje retornar, digite *sair*"
        return evento
    def msg_listmateria():
        evento="Para *listar* as materias pelo nome, utilize *nome_da_materia* ou *numero_da_materia*.\n\nEx1.: _fisica do movimento_\nEx2.: _1110001085_20221_09_\n\nCaso deseje retornar, digite *sair*"
        return evento
    def msg_sem_conta():    
        evento="Não encontramos nenhuma conta com seu numero cadastrada em nosso sistema. Favor digite: *criar conta*"
        return evento
    def msg_consideracoes(usuario):
        evento=f"""Olá, *{usuario}*.
Prazer, eu sou o *Nexus* e também sou um *Little Puccer* assim como você.

Criei este *BOT* com a intenção receber as notificações da PUC dentro do meu WhatsApp.

Como você esta aqui, imagino que possui o mesmo problema que eu de perder ou esquecer das notificações que o Blackboard entrega. Eu sei, é estressante ter que lembrar de tudo não é mesmo?.

Então aqui está meu *projeto salva-vidas* e você pode desfrutar dele o quanto quiser. Espero que goste :).

Quer saber quem eu sou? da uma passadinha lá no meu insta:
*https://www.instagram.com/nexousdn/*"""
        return evento
    def evento_sec(usuario):
        leitura=pd.read_csv("usuarios.csv", sep=';',index_col=["Telefone"]).loc[[int(usuario)]]
        msg = ""
        for (usuario_menu, usuario_nome) in zip(leitura["Menu"], leitura["Apelido"]):
            if usuario_menu=="hub":
                msg=msg_hub()
            elif usuario_menu=="materias":
                msg=msg_materia_menu()
            elif usuario_menu=="rmmateria":
                msg=msg_rmmateria()
            elif usuario_menu=="addmateria":
                msg=msg_addmateria()
            elif usuario_menu=="listmateria":
                msg=msg_listmateria()
            else:   msg=msg_sem_conta()
            msg=msg+f"\n\n*Apelido:* {usuario_nome}\n*Menu:* {usuario_menu}"
        return msg
    def page_test():
        #from whatsbot import page
        a='xpath=//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
        print("Looped")
        return a
    def input_upload():
        a = 'input[name="attach-image"]'
        return a




except Exception:   print("Erro nas defs")


















