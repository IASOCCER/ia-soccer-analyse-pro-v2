import streamlit as st
import pandas as pd
from datetime import datetime

# Estilo CSS customizado para visual mais profissional
st.markdown("""
    <style>
    body {
        background-color: #F8F9FA;
    }
    .main {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
    }
    .card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 1rem;
    }
    .card h2 {
        font-size: 24px;
        margin-bottom: 0.5rem;
        color: #003366;
    }
    .card p {
        font-size: 16px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("<h1 style='color: #003366;'>IA Soccer Analyse Pro</h1>", unsafe_allow_html=True)

# Container principal
st.markdown("<div class='main'>", unsafe_allow_html=True)

# Cartões de estatísticas
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class='card'>
            <h2>25</h2>
            <p>Jogadores Testados</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='card'>
            <h2>87%</h2>
            <p>Testes Concluídos</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class='card'>
            <h2>12</h2>
            <p>Planos Gerados</p>
        </div>
    """, unsafe_allow_html=True)

# Lista dos últimos testes
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("Últimos Testes Registrados")

dados = {
    "Nome do Jogador": ["Lucas E.", "Tracy M.", "Nico S."],
    "Teste": ["Sprint", "Tir", "Agilité"],
    "Data": [datetime.today().date()] * 3,
    "Resultado": ["8.2s", "19 km/h", "17.4s"]
}
df = pd.DataFrame(dados)
st.dataframe(df)

st.markdown("</div>", unsafe_allow_html=True)
