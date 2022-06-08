from datetime import datetime
from time import time
from tkinter import E
from playwright.sync_api import sync_playwright
import time


import unidecode


time_delay = 500
usuario = 'Andre.dal'
senha = 'an@@2019'
usuario_instagram = "ann3.b3ll3_beatriz"
senha_instagram = '12kl34sw'
nome_grupo_insta = '[BOT]'
lista_de_materias = []
botoes_de_volta =[]
botoes_de_volta = [
    '//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a',
    '//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a/div',
    '//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a/svg'
]
lista_de_materias = [
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3406_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3245_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3408_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3303_1&handle=announcements_entry&mode=view",
    "https://eadpucpr.blackboard.com/webapps/blackboard/execute/announcement?method=search&context=course_entry&course_id=_3333_1&handle=announcements_entry&mode=view"
]

mensagem = ''

with sync_playwright() as p:
    browser = p.chromium.launch()

    page = browser.new_page()
    page.goto("https://ava.pucpr.br/blackboardauth/")

    insta = browser.new_page()
    insta.goto("https://www.instagram.com/")
    while True:
        #inicia o login no instagram
        insta.goto("https://www.instagram.com/")
        time.sleep(20)
        print('logando no instagram')
        insta.keyboard.press('Tab')
        time.sleep(1)
        insta.keyboard.press('Tab')
        time.sleep(1)
        insta.keyboard.type(usuario_instagram, delay=1000)
        insta.keyboard.press('Tab')
        time.sleep(1)
        insta.keyboard.type(senha_instagram, delay=1000)
        time.sleep(3)
        insta.keyboard.press('Enter')
        time.sleep(10)
        insta.screenshot(path='insta_login1.png')
        try:
            erro_ao_logar = insta.text_content("text=internet and try", timeout=time_delay)
            insta.screenshot(path='erro_logar_instagram.png')
            print(f'Ohoh, identificamos um erro ao logar no instagram.\no erro encontado foi:\n\n{erro_ao_logar}\n\nDeseja tentar o login novamente com qual conta?')
            print("""
            1. nexousdn
            2. andredalnegro
            3. ann3.b3ll3_beatriz
            4. wapiovesan
            """)
            conta_escolha = int(input('insira o numero desjado: '))
            if conta_escolha == 1:
                usuario_instagram = 'nexousdn'
                senha_instagram = "12kl34SW!"
            if conta_escolha == 2:
                usuario_instagram = 'andredalnegro'
                senha_instagram = "12kl34SW!"
            if conta_escolha == 3:
                usuario_instagram = 'ann3.b3ll3_beatriz'
                senha_instagram - '12kl34sw'
            if conta_escolha == 4:
                usuario_instagram = 'wapiovesan'
                senha_instagram = '12kl34ra'
            else:
                print('escolha errada')

            
        except Exception:
            print(f'Logado com sucesso e sem erros no usuariro {usuario_instagram}.')
            break


    insta.goto('https://www.instagram.com/direct/inbox/')
    time.sleep(4)
    insta.screenshot(path='insta_login2.png')


    

    login_ava_permission = True
    if login_ava_permission == True:
        #procura o ambiente para escrita do nome do usuario
        try:
            page.locator('xpath=//*[@id="user_id"]').click()
            page.locator('xpath=//*[@id="user_id"]').type(usuario)

            #procura o ambiente para escria da senha do usuario
            try:
                page.locator('xpath=//*[@id="password"]').click()
                page.locator('xpath=//*[@id="password"]').type(senha)
                
                #pressiona o botao enter para concluir o login
                try:
                    page.keyboard.press('Enter')
                
                except Exception:
                    print('Erro ao clicar no botao para logar')
            except Exception:
                print('erro ao encontrar barrra de senha')
        except Exception:
            print('erro ao encontrar barra de usuario')

        #procura o botao para aceitacao dos cookies
        while True:
            try:
                page.locator('xpath=//*[@id="agree_button"]').click()
                print('Ava logado com sucesso.')
                break
            except Exception:
                print('botao para aceitar cookies nao foi encontado!')

        #le a entrada do usuario e executa a acao
        def enviar_mensagem(mensagem):
            while True:
                try:
                    clicar_na_conversa = insta.query_selector(f'text={leitura}')
                    clicar_na_conversa.hover(timeout=time_delay)
                    try:
                        clicar_na_conversa.click(timeout=time_delay)
                    except Exception:
                        print('erro no clic diferente')

                    while True:
                        try:
                            insta.locator('xpath=//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').click
                            insta.keyboard.insert_text(mensagem)
                            time.sleep(1)
                            insta.keyboard.press('Enter')
                            print('mensagem enviada.')
                            break
                        except Exception:
                            nexus_lindo = True
                
                    for botao_de_volta in botoes_de_volta:
                        try:
                            insta.locator(f'xpath={botao_de_volta}').click(timeout=time_delay)
                            print('pagina restaurada.')
                        except Exception:
                            nexus_lindo = True
                    break
                except Exception:
                    print('erro na pagina do instagram. Tentando reconectar...')
                    insta.goto('https://www.instagram.com/direct/inbox/')
                    time.sleep(8)
                    insta.screenshot(path='errogeral.png')
                    break

        print('inciando acoes')

        while True:
            #print('loop concluido')
            
            leitura_ja_feita = ''
            leitura = ''

            materia_indice = 10

            try:
                leitura = insta.text_content("text=/", timeout=time_delay)
                evento = leitura.replace('/', '')
                evento = unidecode.unidecode(evento)
                enviar_mensagem(evento)

                #inicia uma serie de IF para reconhecer o dado citado
                if evento == 'feijao':
                    enviar_mensagem('nexinho chupador de buceta')
                    

        
            except Exception:
                nexus_lindo = True


            try:
                leitura = insta.text_content("text=/aviso ética", timeout=time_delay)
                materia_indice = 0
            except Exception:
                nexus_lindo = True

            try:
                leitura = insta.text_content("text=/aviso fdm", timeout=time_delay)
                materia_indice = 1
            except Exception:
                nexus_lindo = True

            try:
                leitura = insta.text_content("text=/aviso lea", timeout=time_delay)
                materia_indice = 2
            except Exception:
                nexus_lindo = True

            try:
                leitura = insta.text_content("text=/aviso mds", timeout=time_delay)
                materia_indice = 3
            except Exception:
                nexus_lindo = True

            try:
                leitura = insta.text_content("text=/aviso pi", timeout=time_delay)
                materia_indice = 4
            except Exception:
                nexus_lindo = True


            #adicionar evento

            try:
                leitura = insta.text_content('text=/adicionar evento', timeout=time_delay)
                enviar_mensagem('')
                evento = leitura.replace('/adicionar evento', '')
                evento = 'evento: ' + evento + ' adicionado com sucesso.'
                enviar_mensagem(evento)
            except Exception:
                nexuslindo = True
            

            

            

            try:
                leitura = insta.text_content("text=/comandos", timeout=time_delay)
                lista_comandos = """
                Lista de comandos de avisos das materias:\n\nLeitura e escrita acadêmica:\n/aviso lea\n\nModelagem de sistemas:\n/aviso mds\n\nProgramação imperativa:\n/aviso pi\n\nÉtica:\n/aviso ética\n\nFísica do movimento\n/aviso fdm
                """
                enviar_mensagem(lista_comandos)
            except Exception:
                nexus_lindo = True
            
            try:
                leitura = insta.text_content("text=nexus lindo", timeout=time_delay)
                enviar_mensagem('Nexus eh gostoso dms')
            except Exception:
                nexus_lindo = True






            if materia_indice < 5:
                print(leitura,' | ', now)
                materia_desejada = lista_de_materias[materia_indice]
                while True:
                    try:
                        page.goto(materia_desejada)
                        break
                    except Exception:
                        print('erro ao entrar na pagina')

                try:
                    mensagem_semanal = page.inner_text('xpath=/html/body/div[6]/div[3]/div/div/div/div/div[3]/form/ul/li[1]', timeout=1000)
                    enviar_mensagem(mensagem_semanal)
                except Exception:
                    print("erro ao ler a mensagem.")
                materia_indice = 10
