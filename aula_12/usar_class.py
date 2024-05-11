from csv_class import CsvProcessor

arquivo_csv = "./exemplo.csv"
filtro = "estado"
limite = "SP"

arquivo = CsvProcessor(arquivo_csv)
arquivo.carregar_csv()
print(arquivo.filtrar(["estado", "preco"], ["SP", "10,50"]))

# arquivo_csv2 = "./exemplo2.csv"
# filtro2 = "estado"
# limite2 = "DF"

# arquivo = CsvProcessor(arquivo_csv2)
# arquivo.carregar_csv()
# print(arquivo.filtrar(filtro2, limite2))
# print(arquivo.sub_filtro("preco", "10,50"))
