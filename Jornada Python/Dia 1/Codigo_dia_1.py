# Passo 01 Entrar no sistema da Empres: Link do sistema da Empresa :https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 02 Logar no sistema
# Passo 03 Importar a base de dados
# Passo 04 Cadastrar 1 produto
# Passo 05 Repetir o processo ate finalizar

import pyautogui
import time

pyautogui.PAUSE = 1 # Da uma pausa para executar o proximo comando
pyautogui.press("win") # Comando para pressionar uma tecla (neste caso a teclah Win)
pyautogui.write("opera") # Comando para escrever (neste caso escrever "chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=628, y=354) # Comando para clicar na posição especificada em x e y
time.sleep(2)
pyautogui.write("Gabriel.j@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")