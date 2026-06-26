#%%
import sys
import os 
sys.path.insert(0, os.path.abspath(".."))
#%%
import pandas as pd
import streamlit as st
import utils.functions as f

#%%
st.set_page_config(initial_sidebar_state="expanded")
st.title('Dashboard analítico 📚')
#%%
df_alunos = f.ler_dados("/home/leosidrim/projects/dashboard_escolar/loader/dados_alunos.xlsx")

#%%
df_alunos
#%%