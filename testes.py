import pyautogui
import time
import pandas

# time.sleep(5)
# print(pyautogui.position())

# Pegando as informações do arquivo excel
tabela = pandas.read_excel(r"C:\Users\jhonatan.souza\Desktop\Vendas - Dez.xlsx")
valorfinal = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

print(quantidade)
print(valorfinal)