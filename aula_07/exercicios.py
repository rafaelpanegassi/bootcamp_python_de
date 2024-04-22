# Exercicío 01: Calcular Média de Valores em uma Lista
# %%
from typing import List


def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)


lista = [4, 5, 6.7, 8.8, 197.27]
resultado = calcular_media(lista)
print(resultado)


# Exercicío 02: Filtrar Dados Acima de um Limite
# %%
def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado


lista = [10, 50, 100, 150, 200, 201, 202, 203, 207.77]
resultado = filtrar_acima_de(lista, 200)
print(resultado)


# Exercicío 03: Contar Valores Únicos em uma Lista
# %%
def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))


lista = [5, 5, 10, 15, 20, 20, 25, 30, 35, 35, 40, 45, 50]
resultado = contar_valores_unicos(lista)
print(resultado)


# Exercicío 04: Converter Celsius para Fahrenheit em uma Lista
# %%
def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9 / 5) * temp + 32 for temp in temperaturas_celsius]


lista = [36.7, 38.9, 43.3, 50, 47.5]
resultado = celsius_para_fahrenheit(lista)
print(resultado)


# Exercicío 05: Calcular Desvio Padrão de uma Lista
# %%
def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia**0.5


lista = [50, 60, 70, 80, 90, 100]
resultado = calcular_desvio_padrao(lista)
print(resultado)


# Exercicío 06: Encontrar Valores Ausentes em uma Sequência
# %%
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))


lista = [1, 2, 3, 4, 6, 7, 9, 11]
resultado = encontrar_valores_ausentes(lista)
print(resultado)
