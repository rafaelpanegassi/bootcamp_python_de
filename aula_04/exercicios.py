#1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# %%
lista: list = []
for i in range(0,11):
    lista.append(i**2)
    print(lista)
    

#2. Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item "C++" e adicione "Ruby".
# %%
lista: list = ['Python', 'Java', 'C++', 'JavaScript']

print('Lista Inicial',lista)

lista.remove('C++')
print('Lista Sem C++',lista)

lista.append('Ruby')
print('Lista Com Ruby',lista)


#3. Para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
# %%
from typing import Dict, Any

livro: Dict[str,int] = { 
    'Titulo' : '1984',
    'Autor':'George Orwell',
    'Ano':1949
} 
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

#4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# %%
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

#5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, 
#calcule o preço total da lista de compras.
# %%
lista: list = ['Maça', 'Banana', 'Cereja']
dicionario: dict = {'Maça':0.45,'Banana':0.30,'Cereja':0.65}

total = sum(dicionario[item] for item in lista)
print(f"Preço total: {total}")

#6. Eliminação de Duplicatas - Dada uma lista de emails, remover todos os duplicados.
# %%
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))
print(emails_unicos)

#7. Filtragem de Dados - Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# %%
idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]
print(idades_validas)

#8. Ordenação Personalizada - Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# %%
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)

#9. Agregação de Dados - Dado um conjunto de números, calcular a média.
# %%
numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)

print("Média:", media)

#10. Divisão de Dados em Grupos - Dada uma lista de valores, dividir em duas listas: 
# uma para valores pares e outra para ímpares.
# %%
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)

#11. Atualização de Dados - Dada uma lista de dicionários representando produtos, 
#atualizar o preço de um produto específico.
# %%
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)

#12. Fusão de Dicionários - Dados dois dicionários, fundi-los em um único dicionário.
# %%
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário -Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
# %%
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)

# 14. Extração de Chaves e Valores - Dado um dicionário, criar listas separadas para suas chaves e valores.
# %%
dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)

# 15. Contagem de Frequência de Itens - Dada uma string, contar a frequência de cada caractere usando um dicionário.
# %%
texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)


#16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# %%
def somar_numeros(lista: list) -> float:
    soma = 0
    for numero in lista:
        soma += numero
    return soma

numeros = [1, 2, 3, 4, 5]
resultado = somar_numeros(numeros)
print("A soma dos números é:", resultado)



#17. Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário.
# %%
def checagem_numero_primo(numero: int) -> int:
    # Verifica se o número é menor que 2, pois números menores que 2 não são primos
    if numero < 2:
        return False
    # Verifica se o número é divisível por algum número entre 2 e a sua metade
    for i in range(2, numero // 2 + 1):
        if numero % i == 0:
            return False
    return True

numero = 17
resultado = checagem_numero_primo(numero)
if resultado:
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")


#18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# %%
def reverter_string(string):
    return string[::-1]

texto = "Olá, mundo!"
texto_revertido = reverter_string(texto)
print("String original:", texto)
print("String revertida:", texto_revertido)

#19. Implemente uma função que receba dois argumentos: uma lista de números e um número. 
#A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# %%
def encontrar_combinacoes(lista, numero):
    combinacoes = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == numero:
                combinacoes.append((lista[i], lista[j]))
    return combinacoes

numeros = [1, 2, 3, 4, 5]
numero_alvo = 7
resultado = encontrar_combinacoes(numeros, numero_alvo)
print("Combinações que somam", numero_alvo, ":", resultado)


#20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
# %%
def ordenar_chaves(dicionario):
    chaves_ordenadas = sorted(dicionario.keys())
    return chaves_ordenadas

meu_dicionario = {"b": 2, "a": 1, "c": 3}
chaves_ordenadas = ordenar_chaves(meu_dicionario)
print("Chaves ordenadas:", chaves_ordenadas)
