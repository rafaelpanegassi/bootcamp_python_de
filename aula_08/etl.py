import glob
import os

import pandas as pd

# 01 - Função de extrair que lê e consolida os JSON's.


def extract_data(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_concat = pd.concat(df, ignore_index=True)
    return df_concat


# 02 - Função que transforma os JSON's.


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


# 03 - Função que carrega os JSON's em parquet ou csv dependendo da escolha.


def load_data(df: pd.DataFrame, output: list):
    for formato in output:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_csv("dados.parquet", index=False)


def pipeline_calculo_vendas_consolidado(diretorio: str, output: list):
    data_01 = extract_data(diretorio)
    data_02 = transform_data(data_01)
    load_data(data_02, output)
