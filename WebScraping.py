from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
navegador = webdriver.Chrome(options=options)
navegador.get('https://www.google.com/')


# 1 -> Pegar a cotação do dólar
# entrar no google
navegador.get("https://www.google.com/")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar", Keys.ENTER)
cotacao_dolar = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_dolar)


# 2 -> Pegar a cotação do euro
navegador.get("https://www.google.com/")
navegador.find_element("xpath", '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro", Keys.ENTER)
cotacao_euro = navegador.find_element("xpath", '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)


# 3 -> Pegar a cotação do ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element("xpath", '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)


# 4 -> Importar a base de dados e atualizar a base
tabela = pd.read_excel("Produtos.xlsx")
print(tabela)


# 5 -> Recalcular os preços
# atualizar a cotação

# cotacao dólar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)

# cotacao euro
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)

# cotacao ouro
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)
print(tabela)

# Recalcular os preços
# preco de compra = cotacao * preco original
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]
# formatar valor para R$
tabela["Preço de Compra"] = tabela["Preço de Compra"].map("R${:.2f}".format) 


# preco de venda = preco de compra * margem
tabela["Preço de Venda"] = tabela["Preço de Venda"] * tabela["Margem"]
# formatar valor para R$
tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)
print(tabela)


# 6 -> Exportar a base atualizada
tabela.to_excel("Produtos Novo.xlsx", index=False)


# fechar navegador
navegador.quit()