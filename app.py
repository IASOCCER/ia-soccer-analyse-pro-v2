import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_option_menu import option_menu

st.set_page_config(page_title="IA Soccer Analyse Pro", layout="wide")

# ---- Funções auxiliares ----
def carregar_dados():
    try:
        return pd.read_csv("dados_jogadores.csv")
    except:
        return pd.DataFrame(columns=["Nome", "Idade", "Altura", "Peso", "Categoria"])

def salvar_dados(df):
    df.to_csv("dados_jogadores.csv", index=False)

# ---- Sidebar com menu ----
with st.sidebar:
    menu = option_menu(
        menu_title="IA Soccer",
        options=["Dashboard", "Jogadores", "Sessão de Testes", "Relatórios"],
        icons=["house", "people", "clipboard-data", "bar-chart"],
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#000814"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "18px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#003566"},
        }
    )

# ---- DASHBOARD ----
if menu == "Dashboard":
    st.title("📊 Painel Principal - IA Soccer Analyse Pro")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("👤 Jogadores Cadastrados", "25")
    with col2:
        st.metric("🧪 Testes Realizados", "122")
    with col3:
        st.metric("📅 Último Teste", "23/07/2025")

    st.markdown("---")
    st.subheader("🔍 Últimos Resultados")
    st.dataframe({
        "Nome": ["Lucas", "João", "Tracy"],
        "Teste": ["Agilidade", "Passe", "Remate"],
        "Nota": ["Muito Bom", "Bom", "A Melhorar"],
        "Data": ["22/07/2025", "21/07/2025", "20/07/2025"]
    })

# ---- JOGADORES ----
elif menu == "Jogadores":
    st.title("📋 Base de Dados de Jogadores")
    dados = carregar_dados()

    with st.expander("➕ Adicionar Novo Jogador"):
        nome = st.text_input("Nome completo")
        idade = st.number_input("Idade", 5, 25, step=1)
        altura = st.number_input("Altura (cm)", 100, 220, step=1)
        peso = st.number_input("Peso (kg)", 20, 120, step=1)
        categoria = st.selectbox("Categoria", ["U8", "U10", "U12", "U14", "U16", "U18"])

        if st.button("Salvar Jogador"):
            novo = pd.DataFrame([[nome, idade, altura, peso, categoria]], columns=dados.columns)
            dados = pd.concat([dados, novo], ignore_index=True)
            salvar_dados(dados)
            st.success("✅ Jogador adicionado com sucesso!")

    st.dataframe(dados)

# ---- TESTES ----
elif menu == "Sessão de Testes":
    st.title("🧪 Sessão de Testes Técnicos")
    st.info("Esta seção será usada para registrar resultados dos testes de passe, condução, agilidade, sprint, reação e remate.")
    st.markdown("---")

    nome = st.selectbox("Selecione o jogador:", carregar_dados()["Nome"].tolist())
    tipo_teste = st.selectbox("Tipo de Teste:", ["Passe", "Condução", "Remate", "Sprint", "Agilidade", "Reação"])
    resultado = st.text_input("Resultado (ex: 15.4s ou 6/6 acertos)")
    observacao = st.text_area("Observações")

    if st.button("Salvar Resultado"):
        with open("resultados_testes.csv", "a") as f:
            f.write(f"{nome},{tipo_teste},{resultado},{observacao},{datetime.now().strftime('%d/%m/%Y')}\n")
        st.success("✅ Resultado salvo com sucesso!")

# ---- RELATÓRIOS ----
elif menu == "Relatórios":
    st.title("📈 Relatórios e Comparações")
    st.warning("Em breve: Comparações por idade, relatórios automáticos com IA e plano de desenvolvimento.")
    st.image("https://cdn-icons-png.flaticon.com/512/5690/5690898.png", width=150)
    st.markdown("---")
    st.info("Você poderá em breve gerar relatórios técnicos completos dos jogadores com base nos testes realizados.")
