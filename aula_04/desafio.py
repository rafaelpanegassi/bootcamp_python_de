def solicitar_dados_usuario() -> tuple[str, float, float]:
    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    while not nome_valido:
        try:
            nome: str = input("Digite seu nome: ")

            # Verifica se o nome está vazio
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            # Verifica se há números no nome
            elif any(char.isdigit() for char in nome):
                raise ValueError("O nome não deve conter números.")
            else:
                print("Nome válido:", nome)
                nome_valido = True
        except ValueError as e:
            print(e)

    while not salario_valido:
        try:
            salario: float = float(input("Digite o valor do seu salário: "))
            if salario < 0:
                print("Por favor, digite um valor positivo para o salário.")
            else:
                salario_valido = True
        except ValueError:
            print("Entrada inválida para o salário. Por favor, digite um número.")

    while not bonus_valido:
        try:
            bonus: float = float(input("Digite o valor do bônus recebido: "))
            if bonus < 0:
                print("Por favor, digite um valor positivo para o bônus.")
            else:
                bonus_valido = True
        except ValueError:
            print("Entrada inválida para o bônus. Por favor, digite um número.")

    return nome, salario, bonus

def calcular_bonus(nome: str, salario: float, bonus: float) -> float:
    bonus_recebido: float = 1000 + salario * bonus  # Exemplo simples de KPI
    return bonus_recebido

def main() -> None:
    nome, salario, bonus = solicitar_dados_usuario()
    bonus_final: float = calcular_bonus(nome, salario, bonus)
    print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")

if __name__ == "__main__":
    main()
