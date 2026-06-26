
import os
import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO = os.path.join(BASE_DIR, "loader", "dados_alunos.xlsx")

def ler_dados() -> pd.DataFrame:
    abas = pd.ExcelFile(ARQUIVO).sheet_names
    frames = []

    for aba in abas:
        meta = pd.read_excel(ARQUIVO, sheet_name=aba, header=None, nrows=2)
        materia  = meta.iloc[0, 0].replace("Matéria: ", "")
        professor = meta.iloc[1, 0].replace("Professor: ", "")

        df = pd.read_excel(ARQUIVO, sheet_name=aba, skiprows=3)

        df["materia"]  = materia
        df["professor"] = professor

        frames.append(df)

    df_final = pd.concat(frames, ignore_index=True)
    df_final.columns = ["id_aluno", "nome_aluno", "turma", "data_prova", "nota", "materia", "professor"]

    return df_final

