import pandas as pd

# 1 -> Importar base da dados
tabela = pd.read_csv("telecom_users.csv") #,sheets=NomeAbaExcel // caso queira criar tabela de uma aba especifica
print(tabela)


# 2 ->  Visualizar a base de dados
# Entender as informações que você tem disponivel
# Descobrir as informações incorretas da base de dados
# axis -> 0 = linha; axis -> 1 = coluna
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)


# 3 -> Tratamento de Dados
# Resolver valores que estão sendo reconhecidos de forma errada
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# Resolver valores vazios

# colunas em que TODOS os valores são vazios, excluir.
# axis -> 0 = linha; axis -> 1 = coluna
tabela = tabela.dropna(how="all", axis=1)

# linhas que tem PELO MENOS 1 valor vazio, excluir.
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())


# 4 -> Análise Inicial
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format)) # <- formatação para porcentagem %


# 5 -> Análise Detalhada - Descobrir causas do cancelamento
# Comparar cada coluna da base de dados com a coluna Churn
import plotly.express as px

# cria grafico
# coluna = "Aposentado"
# grafico = px.histogram(tabela, x=coluna, color="Churn")

# cria grafico
# para cada coluna da minha tabela, criar um grafico

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # exibe o grafico
    grafico.show()


# Conclusoes e Ações.

"""
- Clientes que tem familias maiores tendem a cancelar menos.
    - Promoções diferenciadas para mais pessoas da mesma familia.
- Os clientes nos primeiros meses tem uma tendencia MUITO maior a cancelar
    - Pode ser algum mkt agressivo
    - pode ser que a experiencia nos primeiros meses seja ruim
    - posso fazer uma promoção ano é mais barato
- Tem algum problema no serviço fibra
    - podemos oferecer serviços de graça ou por um preço melhor
- Quase todos os cancelamentos sao do contrato mensal
    - oferecer desconto no anual.
- No boleto o cancelamento é manior, oferecer desconto no cartão
"""