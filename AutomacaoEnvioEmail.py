import pyautogui
import pyperclip
import time
import pandas

pyautogui.PAUSE = 2

# abrindo navegador
pyautogui.hotkey("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(5)

# abrindo nova aba e acessando gmail
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(3)

# acessando arquivo excel e realiza o download
pyautogui.click(x=361, y=345, clicks= 2)
time.sleep(2)
pyautogui.click(x=386, y=420, button= "right")
time.sleep(1)
pyautogui.click(x=467, y=905)
time.sleep(5)
pyautogui.press("enter")

# abre nova aba, acessa a tela inicial do gmail
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# Pegando as informações do arquivo excel
tabela = pandas.read_excel(r"C:\Users\jhonatan.souza\Desktop\curso_ intensivao_python\Vendas - Dez.xlsx")
valorfinal = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()


# envia email
pyautogui.click(x=69, y=165)
time.sleep(1)
pyautogui.write("95jhonatann@gmail.com")
pyautogui.click(x=1282, y=458)
pyperclip.copy("Relatório Vendas - Curso Python")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
email = f"""Olá Prezados!
Segue as informações de vendas:
Valor Final: R${valorfinal:,.2f}
Quantidade: R${quantidade:,}

Att,
Jhonatan Sousa
"""
pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")