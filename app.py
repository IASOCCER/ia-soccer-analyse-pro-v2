import streamlit as st

st.set_page_config(
    page_title="IA Soccer Analyse Pro",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- MENU LATERAL PROFISSIONAL ---
st.sidebar.markdown("## 🧠 IA Soccer Analyse Pro")
menu = st.sidebar.radio("Navegação", [
    "🏠 Dashboard",
    "👥 Jogadores",
    "📝 Sessão de Teste",
    "⚽ Testes Técnicos",
    "📊 Análises Avançadas",
    "📄 Relatórios"
])

# --- CONTEÚDO PRINCIPAL ---
st.markdown(
    f"<h1 style='color:#ffffff;font-size:36px;'>📋 {menu}</h1>",
    unsafe_allow_html=True
)

if menu == "🏠 Dashboard":
    st.success("Painel geral dos resultados e progresso dos jogadores.")

elif menu == "👥 Jogadores":
    st.info("Lista de jogadores registrados e informações pessoais.")

elif menu == "📝 Sessão de Teste":
    st.warning("Inicie e registre uma nova sessão de testes técnicos.")

elif menu == "⚽ Testes Técnicos":
    teste = st.selectbox("Escolha o teste técnico:", [
        "Teste Condução (Illinois)",
        "Teste Passe",
        "Teste Remate",
        "Sprint 10/20m",
        "Agilidade (Zig-Zag)",
        "Reação"
    ])
    st.markdown(f"### {teste}")

elif menu == "📊 Análises Avançadas":
    st.info("Biomecânica, análise de jogo, perfil mental e risco de lesão.")

elif menu == "📄 Relatórios":
    st.info("Geração de relatórios individuais, de sessão e de equipe.")

# --- FOOTER PERSONALIZADO ---
st.markdown(
    "<hr style='border:1px solid #555;'>"
    "<center><small style='color:gray;'>IA Soccer Analyse Pro • Versão 2.0</small></center>",
    unsafe_allow_html=True
)
