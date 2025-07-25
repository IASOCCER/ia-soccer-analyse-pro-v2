import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="IA Soccer Analyse Pro", layout="wide")

# Sidebar com menu moderno
with st.sidebar:
    selected = option_menu(
        menu_title="IA Soccer Analyse Pro",  # título no topo da sidebar
        options=[
            "Dashboard", 
            "Jogadores", 
            "Sessão de Teste", 
            "Testes Técnicos", 
            "Análises Avançadas", 
            "Relatórios"
        ],
        icons=["bar-chart", "person", "clipboard-check", "dribbble", "cpu", "file-earmark-text"],
        menu_icon="cast",  
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#f0f2f6"},
            "icon": {"color": "blue", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"5px"},
            "nav-link-selected": {"background-color": "#4A69BD"},
        }
    )

# Submenu condicional
if selected == "Testes Técnicos":
    submenu = st.selectbox("Escolha o teste:", [
        "Teste Condução (Illinois)",
        "Teste de Passe",
        "Remate",
        "Agilidade",
        "Sprint",
        "Reação",
        "Massa Muscular"
    ])
    st.markdown(f"### {submenu}")

elif selected == "Análises Avançadas":
    submenu = st.selectbox("Escolha a análise:", [
        "Biomecânica IA",
        "Análise de Jogo",
        "Avaliação Mental",
        "Risco de Lesão"
    ])
    st.markdown(f"### {submenu}")

elif selected == "Relatórios":
    submenu = st.selectbox("Tipo de relatório:", [
        "Relatório Individual",
        "Relatório de Sessão",
        "Comparações por Idade"
    ])
    st.markdown(f"### {submenu}")

else:
    st.markdown(f"## {selected}")
    st.success("Bem-vindo ao módulo selecionado.")

