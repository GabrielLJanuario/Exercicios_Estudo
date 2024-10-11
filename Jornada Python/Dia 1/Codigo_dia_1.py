# Passo 01 Entrar no sistema da Empres: Link do sistema da Empresa :https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 02 Logar no sistema
# Passo 03 Importar a base de dados
# Passo 04 Cadastrar 1 produto
# Passo 05 Repetir o processo ate finalizar

import pyautogui
import time
import pandas 

pyautogui.PAUSE = 1 # Da uma pausa para executar o proximo comando
pyautogui.press("win") # Comando para pressionar uma tecla (neste caso a teclah Win)
pyautogui.write("chrome") # Comando para escrever (neste caso escrever "chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=2366, y=375) # Comando para clicar na posição especificada em x e y
time.sleep(2)
pyautogui.write("Gabriel.j@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=2354, y=261)
tabela=pandas.read_csv("Jornada Python/Dia 1/produtos.csv") #Adiciona as informações do arquivo em um arquivo em uma variavel (nesta caso a variavel tabela)

linha=0

for linha in tabela.index: #O tabela.idex no for possibilita que o valor passado pode ser considerado uma linha no python (neste caso o linha sera comparado a um indice na tabela python)
    
    time.sleep(2)
    pyautogui.click(x=2354, y=261)

    codigo=tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca=tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo=tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria=tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco=tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo=tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs=tabela.loc[linha, "obs"]
    pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll()

    linha+=1

