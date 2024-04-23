#Desafio: Análise de Vendas de Produtos
#Objetivo: Dado um arquivo CSV contendo dados de vendas de produtos, o desafio consiste em ler os dados, processá-los em um dicionário para análise e, por fim, calcular e reportar as vendas totais por categoria de produto.

# %%
from etl_type_hint import ler_csv,processar_dados,calcular_vendas_categoria

data = ler_csv("data/vendas.csv")
print(data)
processed_data = processar_dados(data)
print(processed_data)
sales_data = calcular_vendas_categoria(processed_data)
for categoria, total in processed_data.items():
        print(f'{categoria}: ${total}')