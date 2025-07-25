import streamlit as st

# Página inteira
st.set_page_config(page_title="IA Soccer Analyse Pro", layout="wide")

# Sidebar com logo e navegação
st.sidebar.image("https://i.imgur.com/XhL3SV2.png", width=200)  # Substitua pela URL do logo da IA Soccer
st.sidebar.title("IA Soccer Analyse Pro")

menu = st.sidebar.selectbox(
    "Menu Principal",
    [
        "Dashboard",
        "Jogadores",
        "Sessão de Teste",
        "Teste Condução (Illinois)",
        "Teste de Passe",
        "Remate",
        "Massa Muscular",
        "Agilidade",
        "Sprint",
        "Reação",
        "Biomecânica IA",
        "Análise de Jogo",
        "Avaliação Mental",
        "Risco de Lesão",
        "Relatório Individual",
        "Relatório de Sessão",
        "Comparações por Idade"
    ]
)

st.markdown(f"## {menu}")

# Exibição condicional (por enquanto só uma frase por menu para testar)
if menu == "Dashboard":
    st.success("Bem-vindo ao Painel IA Soccer")
elif menu == "Jogadores":
    st.info("Gestão de Jogadores")
elif menu == "Sessão de Teste":
    st.info("Inicie uma nova sessão de testes técnicos")
elif menu == "Teste Condução (Illinois)":
    st.warning("Aqui será o módulo Illinois")
elif menu == "Teste de Passe":
    st.warning("Aqui será o módulo de Passe")
elif menu == "Remate":
    st.warning("Aqui será o módulo de Remate")
elif menu == "Massa Muscular":
    st.info("Aqui será o módulo de Análise Corporal")
# ... e assim por diante


elif menu == "🔬 Biomecanique vidéo":
    page_biomeca()
elif menu == "📝 Rapport Global":
    page_rapport()
