from etl import pipeline_calculo_vendas_consolidado

diretorio: str = "data"
output: list = ["csv", "parquet"]

pipeline_calculo_vendas_consolidado(diretorio, output)
