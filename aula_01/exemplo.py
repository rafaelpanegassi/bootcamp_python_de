## COMANDO PRINT:
# %%
print('Alguma coisa')
# %%
print(3)
# %%
print('Olá' + ' ' + 'Turma')
##################################################################################

## COMANDO INPUT:
# %%
print(input('Digite seu nome: '))
# %%
print('Olá, ' + input('Digite seu nome: ') + '!')

## Exercício 01 - Crie um programa que o usuário digita seu nome e retorna o número de caracteres.
# %%
print(len(input('Digite seu nome: ')))

## Exercício 02 - Crie um programa onde o usuário digite dois valores e apareça a soma.
# %%
print(int(input('Digite um primeiro valor: ')) + int(input('Digite um segundo valor: ')))


## Tipos de Dados Primitivos:
# %%
numero_inteiro = 3
print(numero_inteiro)
type(numero_inteiro)
# %%
numero_decimal = 3.14
print(numero_decimal)
type(numero_decimal)
# %%
texto = 'Rafael'
print(texto)
type(texto)
# %%
booleano = True
print(booleano)
type(booleano)

## Exercício 03 - Refatore o exercicio 02 com variáveis.
# %%
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
print(numero1 + numero2)


