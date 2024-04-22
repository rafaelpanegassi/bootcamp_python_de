# %%
print("Olá, este é meu workspace")


# %%
def soma(valor1_para_somar: float, valor2_para_somar: float) -> float:
    """
    Uma função simples de soma de valores do tipo float que retorna float
    """
    resultado_soma = valor1_para_somar + valor2_para_somar
    return resultado_soma


v1 = 55.5
v2 = 77.3

soma_01 = soma(5, 8.8)
soma_02 = soma(valor1_para_somar=v1, valor2_para_somar=v2)

print(soma_01)
print(soma_02)
