from shutil import ExecError
from numpy import number
import defs
import pandas as pd
import unidecode
def all_ifs(evento, usuario):
    saida=evento
    try:
        command_splited=evento.split()
        #IF mara MENU's
        
        leitura=pd.read_csv("usuarios.csv", sep=';',index_col=["Telefone"]).loc[[int(usuario)]]
        for (usuario_menu, usuario_nome) in zip(leitura["Menu"], leitura["Apelido"]):

            #menu HUB
            if usuario_menu=="hub":
                print(usuario_nome)

                if "1" in command_splited[0]:
                    evento=f"Seu apelido está cadastrado como: _{usuario_nome}_\nSeu numero de telefone é: _{usuario}_"
                elif "2" in command_splited[0]:
                    defs.change_menu(usuario, "materias")
                    evento=""
                elif "9" in command_splited[0]:
                    evento=defs.msg_consideracoes(usuario_nome)
                else:   evento=defs.msg_hub()
                command_splited=[0]


            #menu MATERIAS
            if usuario_menu=="materias":
                if "1" in command_splited[0]:
                    try:    evento = defs.materia_list(evento, usuario)
                    except Exception: evento="erro ao listar materia"
                elif "2" in command_splited[0]:
                    defs.change_menu(usuario, "addmateria");evento= ""
                    break
                elif "3" in command_splited[0]:
                    defs.change_menu(usuario, "rmmateria");evento= ""
                    break
                elif "4" in command_splited[0]:
                    defs.change_menu(usuario, "listmateria");evento= ""
                    break
                elif "9" in command_splited[0]:
                    defs.change_menu(usuario, "hub");evento= ""
                else:   
                    evento= ""




            #menu RM_MATERIA
            if usuario_menu=="rmmateria":
                if not "sair" in command_splited[0]:
                    if evento.isnumeric():
                        try:    evento = defs.remove_materia(evento, usuario);defs.change_menu(usuario, "materias")
                        except Exception: evento="BUUG.\nencontramos um erro ao remover sua materias. Se possivel, reporte esse bug para o nexus";defs.change_menu(usuario, "materias")

                    else:
                        evento="Letra detectada! favor utilizar apenas o ID da matéria"
                else:   defs.change_menu(usuario, "materias");evento="Retornado com sucesso."
            #menu ADD_MATERIA
            if usuario_menu=="addmateria":
                if not "sair" in command_splited[0]:
                    if evento.isnumeric():
                        try:    evento = defs.adicionar_materia(evento, usuario);defs.change_menu(usuario, "materias")
                        except Exception: evento="BUUG.\nencontramos um erro ao adicionar sua materias. Se possivel, reporte esse bug para o nexus";defs.change_menu(usuario, "materias")
                    else:
                        evento="Letra detectada! favor utilizar apenas o ID da matéria"
                else:   defs.change_menu(usuario, "materias");evento="Retornado com sucesso."
            if usuario_menu=="listmateria":
                if not "sair" in command_splited[0]:
                    try:    evento=defs.todas_materias(evento);defs.change_menu(usuario, "materias")
                    except Exception: evento="BUUG.\nencontramos um erro em nossa lista de materias. Se possivel, reporte esse bug para o nexus";defs.change_menu(usuario, "materias")
                else:   defs.change_menu(usuario, "materias");evento="Retornado com sucesso."   


    except Exception:
        print("erro nos IFS")
    
    if saida == evento:
        evento=f'O comando *"{saida}"* nao foi encontrado.'
    return evento












