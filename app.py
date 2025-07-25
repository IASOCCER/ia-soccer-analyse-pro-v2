import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(
    page_title="IA Soccer Analyse Pro",
    page_icon="⚽",
    layout="wide"
)

# --- SIDEBAR ---
with st.sidebar:
    logo = Image.open("logo.png")  # coloque o logo na mesma pasta ou comente esta linha se ainda não tiver
    st.image(logo, width=200)
    st.markdown("## IA Soccer Analyse Pro")
    
    menu_principal = option_menu(
        menu_title=None,
        options=["Dashboard", "Jogadores", "Sessão de Teste", "Testes Técnicos", "Análises Avançadas", "Relatórios"],
        icons=["bar-chart", "people", "clipboard-data", "dribbble", "cpu", "file-earmark-bar-graph"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0!important", "background-color": "#0E1117"},
            "icon": {"color": "white", "font-size": "18px"},
            "nav-link": {"color": "white", "font-size": "16px", "text-align": "left", "margin":"0px"},
            "nav-link-selected": {"background-color": "#4B8BF4"},
        }
    )

# --- CONTEÚDO PRINCIPAL ---
st.markdown(f"<h1 style='color: white;'>{menu_principal}</h1>", unsafe_allow_html=True)

if menu_principal == "Dashboard":
    st.info("📊 Bem-vindo ao painel de controle da IA Soccer.")
    st.write("Aqui você verá os dados resumidos de testes, jogadores e relatórios.")
    
elif menu_principal == "Jogadores":
    st.success("👤 Lista de jogadores registrados.")
    st.write("Em breve: adicionar, buscar e visualizar jogadores.")

elif menu_principal == "Sessão de Teste":
    st.warning("📝 Criação de sessões de teste.")
    st.write("Selecione os jogadores e os testes que serão realizados.")

elif menu_principal == "Testes Técnicos":
    teste_escolhido = st.selectbox("Escolha o teste:", ["Teste Condução (Illinois)", "Teste de Passe"])
    st.subheader(teste_escolhido)
    st.write("Em breve: formulário e análise do teste técnico.")

elif menu_principal == "Análises Avançadas":
    analise = st.selectbox("Selecione a análise:", ["Biomecânica IA", "Avaliação mental", "Risco de lesão"])
    st.subheader(analise)
    st.write("Análise com base em vídeo, IA ou questionários específicos.")

elif menu_principal == "Relatórios":
    st.info("📑 Geração de relatórios PDF.")
    st.write("Relatórios técnicos e físicos serão gerados com base nas sessões.")

# --- ESTILO EXTRA (opcional) ---
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)
