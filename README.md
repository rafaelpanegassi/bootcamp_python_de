# Bootcamp de Python e SQL

## Aula 01

### 01 - Exercícios de `print()`, `input()`, variáveis e estrutura de dados

####  Comandos

####  1) `print()`

O comando `print()` em Python é uma função embutida usada para exibir mensagens ou valores na saída padrão, geralmente no console. Aqui está alguns exemplos:

**Exemplos:**

```python
print("Vamos estudar")
```

```python
print(3 + 5)
```

```python
print("Olá" + " " + "Turma")
```

Ele é uma ferramenta versátil para exibir informações e depurar código durante o desenvolvimento de aplicativos.

#### 2) `input()`

O comando `input()` é uma função embutida em Python que permite que um programa receba entrada do usuário via console. Ele pausa a execução do programa e espera que o usuário insira algum texto, que é então retornado como uma string.

**Exemplos:**

```python
input("Digite seu nome: ")
```

```python
print("Olá, " + input("Digite seu nome: ") + "!")
```

O comando `input()` é uma ferramenta fundamental para criar scripts e programas interativos em Python, permitindo a coleta de dados de entrada de uma maneira fácil e acessível.

#### Considerações Importantes

* **Tipo de Dados**: Por padrão, tudo o que é capturado pelo `input()` é tratado como uma `string`. Se você precisar trabalhar com outro tipo de dado (como inteiros ou floats), será necessário converter a entrada do usuário para o tipo desejado usando funções como `int()` ou `float()`.
    
    ```python
    idade = int(input("Digite sua idade: "))
    ```
    
* **Segurança**: Ao usar `input()` para receber dados do usuário, é importante considerar a validação desses dados, especialmente se eles forem usados em operações críticas ou transmitidos a outras partes do sistema.
    
* **Usabilidade**: O `prompt` deve ser claro e informativo para guiar o usuário sobre o que precisa ser inserido, melhorando a usabilidade e a experiência do usuário.

#### 3) Declaração e Atribuição de Variáveis

Variáveis em Python são fundamentais para o desenvolvimento de programas, pois atuam como "recipientes" para armazenar dados que podem ser modificados ao longo da execução de um script. Ao contrário de algumas outras linguagens de programação, Python é dinamicamente tipado, o que significa que você não precisa declarar explicitamente o tipo de uma variável antes de usá-la. O tipo de uma variável é determinado automaticamente pelo Python no momento da atribuição de um valor.

**Declaração e Atribuição de Variáveis**

A atribuição de um valor a uma variável em Python é feita com o operador `=`. Por exemplo:

```python
numero = 10
mensagem = "Olá, mundo!"
```

No exemplo acima, `numero` é uma variável que armazena um inteiro (`10`), e `mensagem` é uma variável que armazena um texto (`"Olá, mundo!"`).

**Tipos de Dados**

Python suporta vários tipos de dados, incluindo, mas não se limitando a:

* Inteiros (`int`)
* Números de ponto flutuante (`float`)
* Textos (`str`)
* Listas (`list`)
* Tuplas (`tuple`)
* Dicionários (`dict`)
* Booleanos (`bool`)

A linguagem determina o tipo de dados de uma variável no momento da atribuição, o que permite grande flexibilidade, mas também exige atenção para evitar erros de tipo.

**Nomes de Variáveis**

Python tem algumas regras e convenções para nomes de variáveis:

* Os nomes podem conter letras, números e sublinhados (`_`), mas não podem começar com um número.
* Os nomes de variáveis são _case-sensitive_, o que significa que `variavel`, `Variavel`, e `VARIaVEL` são consideradas três variáveis diferentes.
* Existem algumas palavras reservadas que não podem ser usadas como nomes de variáveis, como `if`, `for`, `class`, entre outras.
* É recomendado seguir a convenção _snake_case_ para nomes de variáveis que consistem em mais de uma palavra, como `nome_usuario` ou `total_pedidos`.

**Dinamismo e Reatribuição**

Uma característica importante das variáveis em Python é a possibilidade de reatribuí-las a diferentes tipos de dados:

```python
x = 100        # x é um inteiro
x = "Python"   # Agora x é uma string
```

Isso demonstra a tipagem dinâmica do Python, mas também destaca a importância de gerenciar tipos de dados com cuidado para evitar confusão ou erros em programas mais complexos.

**Escopo de Variáveis**

O escopo de uma variável determina onde ela é acessível dentro do código. Variáveis definidas em um bloco principal são globalmente acessíveis, enquanto variáveis definidas dentro de funções são locais a essas funções, a menos que sejam explicitamente declaradas como `global`.

Entender variáveis e tipos de dados é essencial para programação em Python, pois permite manipular dados de maneira eficaz e criar programas dinâmicos e flexíveis. A capacidade de Python de inferir tipos de dados torna a linguagem acessível para iniciantes, ao mesmo tempo em que oferece poderosas funcionalidades para programadores experientes.

**Exercícios:**

**01 -** Crie programa que o usuário digita o seu nome e retorna o número de caracteres.

**02 -** Criar um programa onde o usuário digite dois valores e apareça a soma.

**03-** Refatore o exercício 02 atribuindo variáveis.

#### Questão: Cálculo de Bônus com Entrada do Usuário

Escreva um programa em Python que solicita ao usuário para digitar seu nome, o valor do seu salário mensal e o valor do bônus que recebeu. O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

#### Instruções:

1. O programa deve começar solicitando ao usuário que insira seu nome.
2. Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
4. O cálculo do KPI do bônus de 2024 é de `1000 + salario + (salario * (bonus/100))`
5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: 
'Olá {nome}, seu novo salário é de {calculo}, já contabilizando seu aumento de {aumento}'.

#### Exemplo de Saída:

Se o usuário digitar "Rafael" como nome, "5000" como salário e "10" como bônus sendo este em porcentagem, o programa deve imprimir:

```bash
Olá Rafel, seu novo salário é de 6500.0, já contabilizando seu aumento de 1500.0
```



## Aula 02

### 01 - TypeError, Type Check, Type Conversion, try-except e if

# TypeError, Type Check e Type Conversion em Python

Python é uma linguagem de programação dinâmica, mas fortemente tipada, o que significa que não é necessário declarar tipos de variáveis explicitamente, mas o tipo de uma variável é determinado pelo valor que ela armazena. Isso introduz a necessidade de compreender como Python lida com diferentes tipos de dados, especialmente quando se trata de operações que envolvem múltiplos tipos. Vamos explorar três conceitos importantes: `TypeError`, verificação de tipo (`type check`), e conversão de tipo (`type conversion`).

## TypeError

Um `TypeError` ocorre em Python quando uma operação ou função é aplicada a um objeto de tipo inadequado. Python não sabe como aplicar a operação porque os tipos de dados não são compatíveis.

### Exemplo de TypeError

Um exemplo clássico é tentar utilizar a função `len()` com um inteiro, o que resulta em `TypeError`, pois `len()` espera um objeto iterável, como uma string, lista, ou tupla, não um inteiro.

```python
# Exemplo que causa TypeError
try:
    resultado = len(5)
except TypeError as e:
    print(e)  # Imprime a mensagem de erro
```

O código acima tenta obter o comprimento de um inteiro, o que não faz sentido, resultando na mensagem de erro: "object of type 'int' has no len()".

## Type Check

Verificação de tipo (`type check`) é o processo de verificar o tipo de uma variável. Isso pode ser útil para garantir que operações ou funções sejam aplicadas apenas a tipos de dados compatíveis, evitando erros em tempo de execução.

### Exemplo de Type Check

Para verificar o tipo de uma variável em Python, você pode usar a função `type()` ou `isinstance()`.

```python
numero = 10
if isinstance(numero, int):
    print("A variável é um inteiro.")
else:
    print("A variável não é um inteiro.")
```

Este código verifica se `numero` é uma instância de `int` e imprime uma mensagem apropriada.

## Type Conversion

Conversão de tipo (`type conversion`), também conhecida como casting, é o processo de converter o valor de uma variável de um tipo para outro. Python oferece várias funções integradas para realizar conversões explícitas de tipo, como `int()`, `float()`, `str()`, etc.

### Exemplo de Type Conversion

Se você quiser somar um inteiro e um número flutuante, pode ser necessário converter o inteiro para flutuante ou vice-versa para garantir que a operação de soma seja realizada corretamente.

```python
numero_inteiro = 5
numero_flutuante = 2.5
# Converte o inteiro para flutuante e realiza a soma
soma = float(numero_inteiro) + numero_flutuante
print(soma)  # Resultado: 7.5
```

### try-except

A estrutura `try-except` é usada para tratamento de exceções em Python. Uma exceção é um erro que ocorre durante a execução do programa e que, se não tratado, interrompe o fluxo normal do programa e termina sua execução. O tratamento de exceções permite que o programa lide com erros de maneira elegante, permitindo que continue a execução ou falhe de forma controlada.

* **try:** Este bloco é o primeiro na estrutura de tratamento de exceções. Python tenta executar o código dentro deste bloco.
* **except:** Se uma exceção ocorrer no bloco `try`, a execução imediatamente salta para o bloco `except`. Você pode especificar tipos de exceção específicos para capturar e tratar apenas essas exceções. Se nenhum tipo de exceção for especificado, ele captura todas as exceções.

#### Exemplo de try-except

```python
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que executa se a exceção ZeroDivisionError for levantada
    print("Divisão por zero não é permitida.")
```

### if

O `if` é uma estrutura de controle de fluxo que permite ao programa executar diferentes ações com base em diferentes condições. Se a condição avaliada pelo `if` for verdadeira (`True`), o bloco de código indentado sob ele será executado. Se a condição for falsa (`False`), o bloco de código será ignorado.

* **if:** Avalia uma condição. Se a condição for verdadeira, executa o bloco de código associado.
* **elif:** Abreviação de "else if". Permite verificar múltiplas condições em sequência.
* **else:** Executa um bloco de código se todas as condições anteriores no `if` e `elif` forem falsas.

#### Exemplo de if

```python
idade = 20
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")
```

Ambas as estruturas, `try-except` e `if`, são fundamentais para a criação de programas em Python que são capazes de lidar com situações inesperadas (como erros de execução) e tomar decisões com base em condições, permitindo assim que você construa programas mais robustos, flexíveis e seguros.