import streamlit as st
import pandas as pd
from datetime import datetime

# ----- ESTILO GLOBAL -----
st.set_page_config(page_title="IA Soccer Analyse Pro", layout="wide")

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
        font-size: 26px;
        margin-bottom: 0.3rem;
        color: #003366;
    }
    .card p {
        font-size: 15px;
        color: #666;
    }
    .menu-title {
        font-size: 24px;
        font-weight: bold;
        color: #003366;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ----- MENU LATERAL -----
menu = st.sidebar.radio("Menu", ["Dashboard", "Jogadores", "Testes Técnicos", "Relatórios"])

# ----- PÁGINA DASHBOARD -----
if menu == "Dashboard":
    st.markdown("<h1 style='color: #003366;'>IA Soccer Analyse Pro - Dashboard</h1>", unsafe_allow_html=True)
    st.markdown("<div class='main'>", unsafe_allow_html=True)

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

# ----- PÁGINA JOGADORES -----
elif menu == "Jogadores":
    st.markdown("<h1 class='menu-title'>Base de Dados dos Jogadores</h1>", unsafe_allow_html=True)
    st.info("⚙️ Esta área será usada para registrar, editar e visualizar os dados completos dos jogadores.")

# ----- PÁGINA TESTES TÉCNICOS -----
elif menu == "Testes Técnicos":
    st.markdown("<h1 class='menu-title'>Testes Técnicos</h1>", unsafe_allow_html=True)
    st.warning("🔧 Em desenvolvimento: testes como Passe, Condução, Sprint, Tir, Agilité, Réaction, etc.")

# ----- PÁGINA RELATÓRIOS -----
elif menu == "Relatórios":
    st.markdown("<h1 class='menu-title'>Relatórios e Comparações</h1>", unsafe_allow_html=True)
    st.success("📊 Aqui serão gerados relatórios automáticos com IA e PDFs por jogador.")

