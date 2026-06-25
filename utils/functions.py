import os
import pandas as pd
import streamlit as st
# Somente Excel
def ler_dados(path) -> pd.DataFrame:
    """
    Função para criação de um dataframe a partir de um arquivo excel 
    """
    df = pd.read_excel(path)
    return df

