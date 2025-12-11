# Requests
# import pyautogui 
# from time import sleep

#BOT DE MINERAÇÃO
#chegando até o lugar da mineração
# sleep(2)
# pyautogui.moveTo(702,511, duration=1)

# for i in range(100):
#     pyautogui.leftClick()
#     sleep(0.2)
# print("Fim do script")

##########################################################################

#BOT ESPECIALISTA EM CLIQUES
#Trata-se de um script mais detalhado da função de clicar
# sleep(2)
# pyautogui.click(x=840, y= 918, clicks=2, interval=0.0, button="left", duration=0.2)
#clicks=2 é a quantidade de clicks que queremos - o método click, por default é realizado com o botão esquerdo do mouse, porém, também temos as funções
#prontas, como a leftClick(), rightClick(), doubleClick(), tripleClick() e middleClick().
#interval=0.0 é o intervalo entre os clicks
#button="left" é o botão que queremos usar
#duration=0.2 é o tempo que leva para o cursor ir até a posição

##########################################################################

#DESAFIO PARA A CRIAÇÃO DE UMA NOVA PASTA
# sleep(2)
# pyautogui.moveTo(1711,516, duration=1)
# sleep(0.5)
# pyautogui.rightClick()
# sleep(0.5)
# pyautogui.move(-50,160, duration=1)
# sleep(0.5)
# pyautogui.click(button="left")
# sleep(0.5)
# pyautogui.move(-400,0, duration=0.5)
# sleep(0.5)
# pyautogui.click(button="left")
# sleep(0.5)
# pyautogui.write("Testando escrever o t", interval=0.05)
# sleep(0.05)
# pyautogui.press("´")
# sleep(0.05)
# pyautogui.write("itulo de uma nova pasta", interval=0.05)
# pyautogui.press("enter")
# print("Fim do script")

##########################################################################

#1 DESAFIO PARA A CRIAÇÃO DE UM BOT DE VARREDURA DE DOCUMENTOS EM UMA PASTA E MANDAR A OUTRA

#Exemplo de utilização: ter uma pasta que seja alimentada com publicadades e deixar o whatsapp web ligado e essa automação iria 
#transferir todas as publicidades para o whatsapp web automaticamente e enviar as mensagens.

# #Requerimentos
# import pyautogui
# import time

# time.sleep(4)

# #Criando o laço de repetição para fazer a transferência dos arquivos
# for i in range(43):
#     # move o mouse até a posição desejada
#     pyautogui.moveTo(1084,288, duration=0.5)
#     # clica no elemento de transferência, arrasta até o outro ponto e solta o arquivo
#     pyautogui.dragTo(1800,468, button="left", duration=0.5)
#     time.sleep(0.5)

# pyautogui.alert("Transferência concluída!")

##########################################################################

# 2 DESAFIO PARA A CRIAÇÃO DE UM BOT DE VARREDURA DE DOCUMENTOS EM UMA PASTA E MANDAR A OUTRA

# import os
# import time
# import pyautogui

# # Caminho da pasta de origem e destino
# pasta_origem =  pyautogui.prompt("Digite o caminho da pasta de origem:", default=r"C:\Users\Francisco\Documents\Origem")
# pasta_destino = pyautogui.prompt("Digite o caminho da pasta de destino:", default=r"C:\Users\Francisco\Documents\Destino")

# # Lista todos os arquivos da pasta (ignorando subpastas)
# arquivos = [f for f in os.listdir(pasta_origem) if os.path.isfile(os.path.join(pasta_origem, f))]

# # Mostra quantos arquivos foram encontrados
# pyautogui.alert(f"Foram encontrados {len(arquivos)} arquivos para processar.")

# # Loop dinâmico baseado no número real de arquivos
# for i, arquivo in enumerate(arquivos, start=1):
#     print(f"Processando arquivo {i}/{len(arquivos)}: {arquivo}")

#     # Exemplo: ação com PyAutoGUI (substitua pelo que o seu robô faz)
#     pyautogui.hotkey('ctrl', 'c')  # Exemplo de cópia
#     time.sleep(1)
#     pyautogui.hotkey('ctrl', 'v')  # Exemplo de colagem
#     time.sleep(1)

#     # (Opcional) mover arquivo para a pasta de destino
#     caminho_origem = os.path.join(pasta_origem, arquivo)
#     caminho_destino = os.path.join(pasta_destino, arquivo)
#     os.rename(caminho_origem, caminho_destino)

# pyautogui.alert("Processamento concluído!")

##########################################################################

# 3 DESAFIO PARA A CRIAÇÃO DE UM BOT DE VARREDURA DE DOCUMENTOS EM UMA PASTA E MANDAR A OUTRA MAIS MODERNO COM PROCESSAMENTO EM TELA

# import os
# import time
# import shutil
# import tkinter as tk
# from tkinter import filedialog, messagebox, ttk

# # ==============================
# # 1️⃣ Seleção das pastas
# # ==============================
# root = tk.Tk()
# root.withdraw()  # Oculta a janela principal do tkinter

# pasta_origem = filedialog.askdirectory(title="Selecione a pasta de ORIGEM")
# if not pasta_origem:
#     messagebox.showerror("Erro", "Você não selecionou a pasta de origem.")
#     exit()

# pasta_destino = filedialog.askdirectory(title="Selecione a pasta de DESTINO")
# if not pasta_destino:
#     messagebox.showerror("Erro", "Você não selecionou a pasta de destino.")
#     exit()

# # ==============================
# # 2️⃣ Coleta dos arquivos
# # ==============================
# arquivos = [f for f in os.listdir(pasta_origem) if os.path.isfile(os.path.join(pasta_origem, f))]

# if not arquivos:
#     messagebox.showinfo("Aviso", "Nenhum arquivo encontrado na pasta de origem.")
#     exit()

# total_arquivos = len(arquivos)

# # ==============================
# # 3️⃣ Criação da janela de progresso
# # ==============================
# janela = tk.Tk()
# janela.title("Processamento de Arquivos")
# janela.geometry("550x160")
# janela.resizable(False, False)

# # Label principal
# label_titulo = tk.Label(janela, text="Processando arquivos...", font=("Segoe UI", 12, "bold"))
# label_titulo.pack(pady=10)

# # Label de status
# label_status = tk.Label(janela, text=f"Iniciando processamento de {total_arquivos} arquivos...", font=("Segoe UI", 10))
# label_status.pack(pady=5)

# # Barra de progresso
# progress = ttk.Progressbar(janela, orient="horizontal", length=500, mode="determinate")
# progress.pack(pady=10)
# progress["maximum"] = total_arquivos
# progress["value"] = 0

# # ==============================
# # 4️⃣ Função principal de processamento
# # ==============================
# def processar():
#     for i, arquivo in enumerate(arquivos, start=1):
#         # Atualiza label de status
#         label_status.config(text=f"Processando arquivo {i}/{total_arquivos}: {arquivo}")
#         janela.update_idletasks()

#         # Caminhos completos
#         origem = os.path.join(pasta_origem, arquivo)
#         destino = os.path.join(pasta_destino, arquivo)

#         # Simulação de automação (substitua aqui pelo seu código PyAutoGUI)
#         time.sleep(0.3)  # Pausa simulando tempo de execução
        
#         # Move o arquivo após "processar"
#         try:
#             shutil.move(origem, destino)
#         except Exception as e:
#             print(f"⚠️ Erro ao mover {arquivo}: {e}")

#         # Atualiza a barra de progresso
#         progress["value"] = i
#         janela.update_idletasks()

#     # Finalização
#     label_status.config(text="✅ Todos os arquivos foram processados com sucesso!")
#     messagebox.showinfo("Concluído", f"{total_arquivos} arquivos foram processados e movidos com sucesso.")
#     janela.destroy()

# # ==============================
# # 5️⃣ Inicia o processamento
# # ==============================
# janela.after(1000, processar)
# janela.mainloop()


##########################################################################

# 2 USANDO A ROLAGEM DO MOUSE - FUNÇÃO SCROLL() - VERSÃO 1 - INSTAGRAM

#Esta função é importante para quando precisamos rolar uma página para baixo ou para cima, por exemplo para acessarmos links
#ou listas de usuários em caixas de diálogos.

# import pyautogui
# from time import sleep

# # Num primeiro exemplo vamos rolar a página de seguidores do instagram. Com a janela do Instagram, usuários aberta de forma minimizada
# # no canto da tela, vamos:
# # levar o mouse até a caixa de diálogo

# #Inserir um sleep de espera para que eu abra a janela do instagram
# sleep(3)
# pyautogui.moveTo(1669,580, duration=0.5)
# pyautogui.moveTo(1665,380, duration=0.5)

# #Agora vamos rolar a página para baixo
# for i in range(5):
#     pyautogui.scroll(-1500) # a função é parametrizada em pixeis, para cima ou para baixo.
#     sleep(1)

##########################################################################

# AUTOMAÇÃO DE SISTEMAS USANDO BOTOES DO TECLADO - FUNÇÃO HOTKEY()

#a função hotkey é a que serve para pressionar dois botões ao mesmo tempo.

# Para tal usei o site de teste: https://www.ethos.org.br/teste-login/

# COMANDO PARA ABRIR A LISTA DE COMANDOS DAS TECLAS: print(PYAUTOGUI.KEYBOARD_KEYS)
#['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

# import pyautogui
#buscar uma senha
# pyautogui.click(1392,195, duration=0.5)
# sleep(0.5)
# pyautogui.hotkey("ctrl", "c")
# sleep(0.5)
# pyautogui.click(1395,251, duration=0.5)
# sleep(0.5)
# pyautogui.hotkey("ctrl", "v")


# pyautogui.click(1083,516, duration=1)
# sleep(0.5)
# pyautogui.write("chico_ilha@hotmail.com", interval=0.05)
# sleep(0.5)
# pyautogui.press("tab")
# sleep(0.5)
# pyautogui.write("Senha1234", interval=0.05)
# sleep(0.5)
# pyautogui.click(1081,688, duration=0.5)
# sleep(0.5)
# pyautogui.click(1423,799, duration=0.5)

##########################################################################

# CRIANDO UM ALERTA

# import pyautogui

# pyautogui.alert(text="Este é um alerta simples!", title="Alerta do PyAutoGUI", button="OK")

##########################################################################

# SOLICITANDO INFORMAÇÕES DO USUÁRIO - INPUT BOX

# import pyautogui

# nome = pyautogui.prompt(text="Qual é o seu nome?", title="Caixa de Entrada do PyAutoGUI", default="Seu nome aqui")

# pyautogui.alert(f"Seja bem vindo, {nome}.")

#CASO A INFORMAÇÃO SEJA UMA SENHA:

# import pyautogui

# senha= pyautogui.password(text="Digite sua senha:", title="Caixa de Senha do PyAutoGUI", default="", mask="*")


##########################################################################

# AUTOMAÇÃO PARA PREENCHIMENTO DE LOGIN COM INFORMAÇÕES DE LOGIN E SENHA DE USUÁRIO

# Página para teste: https://www.ethos.org.br/teste-login/

# Requerimento
# import pyautogui
# from time import sleep

# # coleta da informação de login
# login = pyautogui.prompt(text="Digite seu login de usuário:", title="Login do Usuário", default="seu_login_aqui")
# sleep(0.5)
# # preenchimento da resposta na página
# pyautogui.click(1475,453, duration=0.5)
# sleep(0.5)
# pyautogui.write(login, interval=0.05)
# sleep(0.5)

# pyautogui.press("tab")
# sleep(1)

# # coleta da informação de senha
# senha = pyautogui.password(text="Digite sua senha:", title="Senha do Usuário", default="", mask="*")
# sleep(0.5)

# # preenchimento da resposta na página
# pyautogui.write(senha, interval=0.05)
# sleep(0.5)
# pyautogui.click(1454,632, duration=0.5)
# sleep(0.5)
# pyautogui.click(1665,740, duration=0.5)
##############################################################################

# 2 USANDO A ROLAGEM DO MOUSE - FUNÇÃO SCROLL() - VERSÃO 2 - WIKIPEDIA

# Página utilizada para o exemplo: https://pt.wikipedia.org/wiki/Brasil?_gl=1*2ii28k*_ga*MTU3NTM0OTk0My4xNzYwOTc2Njk5*_ga_37GXT4VGQK*czE3NjIzNjE0NTYkbzExJGcxJHQxNzYyMzYxOTM3JGo0MiRsMCRoMA..

# import pyautogui
# from time import sleep

# # clicando no edge
# pyautogui.click(826,1057, duration=0.5)
# sleep(2)
# pyautogui.click(768,54)
# sleep(2)
# pyautogui.write("https://pt.wikipedia.org/wiki/Brasil?_gl=1*2ii28k*_ga*MTU3NTM0OTk0My4xNzYwOTc2Njk5*_ga_37GXT4VGQK*czE3NjIzNjE0NTYkbzExJGcxJHQxNzYyMzYxOTM3JGo0MiRsMCRoMA")
# sleep(5)
# pyautogui.press("enter")
# sleep(2)
# pyautogui.move(0,100, duration=0.5)
# sleep(2)
# pyautogui.scroll(-2600)
# sleep(2)
# pyautogui.click(264,481, duration=0.5)
# sleep(1)
# pyautogui.click(1896,17, duration=0.5)
# sleep(0.5)
# pyautogui.alert("Automação realizada com sucesso!")

##############################################################################

# BOT DE SOLICITAÇÃO DE INFORMAÇÕES E PREENCHIMENTO EM SITE DE LOGIN

# import pyautogui
# from time import sleep

# #site utilizado para o projeto: https://www.ethos.org.br/teste-login/

# #Clicando no campo de login
# pyautogui.click(1492,449, duration=0.5)
# sleep(0.5)

# # solicitando a informação do login
# login = pyautogui.prompt(text="Digite seu login de usuário:", title="Login do Usuário", default="seu_login_aqui")
# sleep(0.5)
# # preenchendo o campo de login
# pyautogui.write(login, interval=0.05)
# sleep(0.5)
# pyautogui.press("tab")
# sleep(1)
# # solicitando a informação da senha
# senha = pyautogui.password(text="Digite sua senha:", title="Senha do Usuário", default="", mask="*")
# sleep(0.5)
# # preenchendo o campo da senha
# pyautogui.write(senha, interval=0.05)
# sleep(0.5)

# # clicando no botão de não sou robo
# pyautogui.click(1455,621, duration=0.5)
# sleep(0.5)
# # clicando no botão de entrar
# pyautogui.click(1657,729, duration=0.5)
# sleep(0.5)
# pyautogui.alert(text="Login realizado com sucesso!", button="OK")

##############################################################################

# NOVO INTERVALO ENTRE UMA TIVIDADE E OUTRA - FUNÇÃO PAUSE

# import pyauogui as pg

# pg.PAUSE = 1 #Aqui estou definindo um intervalo de 1 segundo entre cada ação do PyAutoGUI

# #Ou seja, agora não precisamos mais definir a cada atividade um sleep, pois o PyAutoGUI já fará isso automaticamente.

# FORMA DE DEIXAR O TEMPO DE ESPERA ALEATÓRIO ENTRE AS ATIVIDADES
# import random

# pg.PAUSE =  random.randint(1,3) #Aqui estou definindo um intervalo aleatório entre 1 e 3 segundos entre cada ação do PyAutoGUI

# FORMA DE CANCELAR A POSSIBILIDADE DE CANCELAR A AUTOMAÇÃO COM O MOVIMENTO DO MOUSE PARA O CANTO SUPERIOR ESQUERDO DA TELA
# pg.FAILSAFE = False

##############################################################################

# # ZERANDO UM NOVO JOGO COM PYAUTOGUI

# import pyautogui as pg
# import random

# #pg.PAUSE=random.randint(1,3)

# # Mover o mouse até a posição
# pg.moveTo(1632,549, duration=0.5)

# for i in range(1001):
#     pg.click()

# pg.alert("The rock is gone!")

##############################################################################

# RECONHECIMENTO DE IMAGEM COM OPENCV E PYAUTOGUI

# # Como fazer reconhecimento de imagem simples
# import pyautogui as pg

# pg.PAUSE = 1
# # Como encontrar algo na tela
# # box = pg.locateOnScreen('5.png')
# # print(box)
# # ponto_central = pg.locateCenterOnScreen('5.png')
# # print(ponto_central)
# # if ponto_central:
# #     pg.click(ponto_central,duration=2)
# # Parãmetros avançados
# '''
# # confidence (0.0 a 1.0) 
#    - Define o nível de similaridade necessário para considerar um match
#    - 1.0 = match perfeito (100%)
#    - 0.9 = 90% de similaridade (padrão recomendado)
#    - 0.7 = 70% de similaridade (mais flexível)
#    - ⚠️ REQUER: pip install opencv-python
#    - 💡 Para aumentar chances de encontrar: reduza para 0.7-0.8
# # grayscale (True/False)
#    - True = Busca em escala de cinza (mais rápido, ~30%)
#    - False = Busca colorida (padrão)
#    - 💡 Use True se as cores não importam para identificação
# # minSearchTime (segundos)
#    - Tempo mínimo que o PyAutoGUI vai procurar antes de retornar None
#    - Útil quando a imagem pode demorar para aparecer
#    - Padrão: 0 (busca instantânea)
# '''
# ponto_central = pg.locateCenterOnScreen(
#     'botao-captcha.png', # nome do arquivo
#     confidence=0.70, # nível de confidence
#     grayscale=False, # se deve usar grayscale
#     minSearchTime=2
# )
# print(ponto_central)
# if ponto_central:
#     pg.click(ponto_central,duration=2)
# # Como usar em automações e para quebrar captchas

##############################################################################

# BOT DE CURTIDAS NO INSTAGRAM

# # Projeto de Automação do Instagram - Bot de curtidas
# import pyautogui as pg
# import pyperclip
# from time import sleep

# def write_pro(frase):
#     pyperclip.copy(frase)
#     pg.hotkey('ctrl', 'v')

# pg.PAUSE = 2
# # site - https://instaclone-devaprender.netlify.app/
# # Seu desafio
# # Logar no instagram - jhonatan / senha123
# campo_usuario = pg.locateCenterOnScreen(
#     'campo_usuario.png',
#     confidence=0.70,
#     minSearchTime=2
#     )

# pg.click(campo_usuario,duration=2)
# pg.write('jhonatan')
# pg.press('tab')
# pg.write('senha123')
# pg.press('tab')
# pg.press('space')

# sleep(5)
# # clicar na primeira postagem
# botao_comentar = pg.locateCenterOnScreen('botao_comentar.png',confidence=0.70,minSearchTime=2)
# pg.click(botao_comentar,duration=2)

# # clicar em curtir
# botao_curtir = pg.locateCenterOnScreen('botao_curtir.png',confidence=0.70,minSearchTime=2)
# pg.click(botao_curtir,duration=2)

# # clicar em comentar
# botao_comentar = pg.locateCenterOnScreen('botao_comentar.png',confidence=0.70,minSearchTime=2)
# pg.click(botao_comentar,duration=2)

# write_pro('bitcoin é demais!')

# # clico  no botão de enviar o comentario
# botao_enviar_comentario = pg.locateCenterOnScreen('botao_enviar_comentario.png',confidence=0.70,minSearchTime=2)
# pg.click(botao_enviar_comentario,duration=2)
# # curtir a foto
# # deixar um comentário

