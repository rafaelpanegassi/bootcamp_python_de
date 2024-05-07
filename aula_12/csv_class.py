import pandas as pd


class CsvProcessor:
    def __init__(self, path: str):
        self.path = path
        self.df = None
        self.df_filtrado = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.path)
        return self.df

    def filtrar(self, coluna, atributo):
        self.df_filtrado = self.df[self.df[coluna] == atributo]
        return self.df_filtrado

    def sub_filtro(self, coluna, atributo):
        return self.df_filtrado[self.df_filtrado[coluna] == atributo]


# arquivo_csv = './exemplo.csv'
# filtro = 'estado'
# limite = 'SP'
#
# arquivo = CsvProcessor(arquivo_csv)
# arquivo.carregar_csv()
# print(arquivo.filtrar(filtro,limite))
# print(arquivo.sub_filtro('preco','10,50'))
#
# arquivo_csv2 = './exemplo2.csv'
# filtro2 = 'estado'
# limite2 = 'DF'
#
# arquivo = CsvProcessor(arquivo_csv2)
# arquivo.carregar_csv()
# print(arquivo.filtrar(filtro2,limite2))
# print(arquivo.sub_filtro('preco','10,50'))
