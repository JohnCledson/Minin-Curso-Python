import pandas as pd

# Importar a base de dados
tabela_vendas = pd.read_excel('venv/Vendas.xlsx')

# Visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# Faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

# Quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

# Ticket medio por produto em cada loja

# Envia um email com o relatório