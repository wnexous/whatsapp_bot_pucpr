import time
from playwright.sync_api import sync_playwright
import unidecode
import random
from time import strftime; import pandas as pd; from datetime import date, datetime
import defs
import if_finds
from imp import reload

hub_group_name = "[HUB] Nexous"

usuario_atual = []; adicionar_evento =[]; adicionar_evento = []; new_list = []; usuario_listados = [];evento = ''
lista_de_materias = [
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3406_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3245_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3408_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3303_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3333_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3675_1&handle=announcements_entry&mode=view"
]
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page();whats=context.new_page()

    whats.goto("https://web.whatsapp.com/")
    #procura o ambiente para escrita do nome do usuario
    def login_ava():
        try:
            page.goto("https://ava.pucpr.br/blackboardauth/")
            #page.locator('xpath=//*[@id="user_id"]').click()
            page.locator('xpath=//*[@id="user_id"]').type('usuario_puc')

            #procura o ambiente para escria da senha do usuario
            try:
                #page.locator('xpath=//*[@id="password"]').click()
                page.locator('xpath=//*[@id="password"]').type('senha_puc')
                
                #pressiona o botao enter para concluir o login
                try:
                    page.keyboard.press('Enter')
                
                except Exception:
                    print('Erro ao clicar no botao para logar')
            except Exception:
                print('erro ao encontrar barrra de senha')
        except Exception:
            pass
        #procura o botao para aceitacao dos cookies
        try:
            page.locator('xpath=//*[@id="agree_button"]').click()
            print('Ava logado com sucesso.')
        except Exception:
            pass
        evento = 'ava logado com sucesso.'
        return evento
    #login_ava()
    while True:
        try:
            print(whats.text_content(f'text={hub_group_name}', timeout=200))
            print('Logado com sucesso.')
            break
        except Exception:
            pass
        print('esperando reconhecer login no whatsapp')    
        whats.screenshot(path="dentroDoZap.png")
    def reload_page():
        try:
            whats.goto("https://web.whatsapp.com/")
            whats.screenshot(path="dentroDoZap.png")
        except Exception:
            print('erro ao dar reload')
    def hub(hub_group_name):
        try:
            whats.locator(f"text={hub_group_name}").click(timeout=10000)
        except Exception:
            print('erro ao retornar ao hub.')
            whats.screenshot(path="erro_hub.png")
    def aviso_ava(materia_idice, lista_de_materias):
        while True:
            try:
                page.goto(lista_de_materias[materia_idice])
                try:
                    whats.keyboard.insert_text(page.text_content('xpath=//*[@id="crumb_1"]', timeout=2000))
                    whats.keyboard.press('Enter')
                except Exception:
                    pass
                    
                try:
                    evento = page.text_content('xpath=/html/body/div[6]/div[3]/div/div/div/div/div[3]/form/ul/li[1]', timeout=1000)
                    break
                except Exception:
                    try:
                        evento = page.text_content('xpath=/html/body/div[5]/div[3]/div/div/div/div/div[3]/form/ul/li[1]', timeout=1000)
                        break
                    except Exception:
                        try:
                            whats.keyboard.insert_text('opa chefia, vi aqui que meu ava esta deslogado. vou reconectar aqui novamente')
                            whats.keyboard.press('Enter')
                        except Exception:
                            pass
                        evento = login_ava()
            except Exception:
                evento = login_ava()
            evento = evento.replace('\t', '')
            evento = evento.replace('  ', '')
            evento = evento.replace('	', '')
        return evento
    def nome_grupo():
        try:
            nome_grupo = whats.text_content('xpath=//*[@id="main"]/header/div[2]/div[1]/div/span')
            saida=''
            for x in nome_grupo:
                if x.isnumeric():
                    saida+=x
            return saida
        except Exception:
            evento = "Nao foi possivel captar o nome do grupo."
            return evento
    while True:
        try:
            #inicia um reconhecomento de texto mais rapido
            leitura = ''
            confimacao_leitura=''
            
            while True:
                try:
                    receb = whats.locator("._2nY6U.vq6sj._3C4Vf ._3OvU8 ._37FrU ._1qB8f .Hy9nV .ggj6brxn")
                    evento = receb.text_content()
                    receb.click()
                    print(f'[{datetime.today().strftime("%H:%M:%S")}]', evento)
                    break
                except Exception:   pass
            #Reconhece o texto digitado e limpa acentuacoes
            evento = unidecode.unidecode(evento)
            evento = evento.lower()
            reconhecimento = evento.strip()
            saida = evento
            nome_usuario=nome_grupo()

            #Inicia o reconhecimento baseado em IF
            reload(if_finds)
            reload(defs)

            if "criar conta" in evento:
                evento=evento.replace("criar conta ", "").replace("criar conta", "")
                if not evento == "":
                    evento = defs.criar_conta(evento.replace("criar conta ", "").replace("criar conta", ""), nome_grupo())
                else:   evento = "Faltou adicionar apelido! Digite *criar conta seu_apelido*"
            else:   
                try:
                    print(pd.read_csv("usuarios.csv", sep=';',index_col=["Telefone"]).loc[[int(nome_usuario)]])
                    evento = if_finds.all_ifs(reconhecimento, nome_usuario)
                except Exception:
                    evento = f"Ooops, parece que voce ainda nao tem uma conta!. Digite *criar conta*"
        
            try:    whats.keyboard.insert_text(evento);whats.keyboard.press('Enter')
            except Exception:   pass
            
            try:    whats.keyboard.insert_text(defs.evento_sec(nome_usuario));whats.keyboard.press('Enter')
            except Exception:   pass
                
            
            print(f'[{datetime.today().strftime("%H:%M:%S")}] cliclo completo')
            hub(hub_group_name)
                
        except Exception:
            page.screenshot(path="erro_page.png")
            whats.screenshot(path="erro_whats.png")
            try:
                whats.keyboard.insert_text('Ocorreu um erro')
                whats.keyboard.press('Enter')
                hub()
            except Exception:
                pass
            print('erro encontrado e reportado')