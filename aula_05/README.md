# Um Bilhão de Linhas: Desafio de Processamento de Dados com Python

Este repositório representa o Projeto_01 do BOOTCAMP de Engenharia de Dados, cujo objetivo é comparar diferentes formas de ler um bilhão de linhas em Python. O objetivo é implementar modificações nos scripts com base nos conceitos aprendidos nas aulas anteriores do bootcamp, como dicas de tipos e funções.


## Resultados

Especificações da Máquina Utilizada:
* Ryzen 5 3600
* 32G RAM

|           Ambiente    | Tempo de Execução   |
|-------------------|------------------:|
| Python            |      42 min 37 s    |
| Python + Pandas   |       5 min 42 s    |
| Python + Polars   |        27 s    |
| Python + Duckdb   |        24 s    |


## Como executar

Como executar este projeto utilizando `pyenv` and `poetry`.

Antes de executar o projeto, não esqueça de colocar o arquivo *measurements.txt* dentro do `.gitignore`

1. Clone este repositorio:
```bash
git clone https://github.com/rafaelpanegassi/bootcamp_jornada.git
```
 2. Entre nesta pasta:
 ```bash
 cd bootcamp_jornada/aula_05
 ```

3. Coloque a versão do python usando pyenv:
```bash
pyenv local 3.12.1
```

4. Coloque a versão do python usando poetry:
```bash
poetry env use 3.12.1
``` 

5. Instale todas as dependências e entre no ambiente virtual:
```bash
poetry install --no-root
```
```bash
poetry lock --no-update
```
```bash
poetry shell
```

6. Criar o arquivo *measurements.txt*:
```bash
python src/create_measurements.py
```

7. Ler os arquivos de cada script especifico:
```bash
python src/using_python.py 
```
```bash
python src/using_pandas.py 
```
```bash
python src/using_polars.py 
```
```bash
python src/using_duckdb.py 
```

--------------
Conteúdo original está neste [Repositório Oficial](https://github.com/lvgalvao/One-Billion-Row-Challenge-Python)!