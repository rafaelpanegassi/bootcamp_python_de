#Desafio - Refatorar o projeto da aula anterior na solução anterior para que se o usuario digitar alguma informação
#incorreta, o programa repetir para que ele digite novamente até que ele coloque todas as informações corretas,
#evitando que quando ele coloque alguma informação correta o programa trave!

# %%
# Setando as variaveis para controle do loop:
nome_correto = False
salario_correto = False
bonus_recebido_correto = False
# Solicita ao usuário que digite seu nome
while not nome_correto:
    try:
        nome = input('Digite seu nome: ')
        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError('O nome não pode estar vazio.')
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError('O nome não deve conter números.')
        else:
            print('Nome válido:', nome)
            nome_correto = True
    except ValueError as e:
        print(e)
# Solicita ao usuário que digite o valor do seu salário e converte para float
while not salario_correto:
    try:
        salario = float(input('Digite o valor do seu salário: '))
        if salario < 0:
            print('Por favor, digite um valor positivo para o salário.')
        else:
            print('Salario válido:',salario)
            salario_correto = True
    except ValueError:
        print('Entrada inválida para o salário. Por favor, digite um número.')
# Solicita ao usuário que digite o valor do bônus recebido e converte para float
while not bonus_recebido_correto:
    try:
        bonus_recebido = float(input("Digite o valor do bônus recebido: "))
        if bonus_recebido < 0:
            print("Por favor, digite um valor positivo para o bônus.")
        else:
            print('Bonus recebido válido: ',bonus_recebido)
            bonus_recebido_correto = True
    except ValueError:
        print("Entrada inválida para o bônus. Por favor, digite um número.")
# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")