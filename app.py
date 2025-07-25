import streamlit as st
from streamlit_option_menu import option_menu

# Configurações da página
st.set_page_config(page_title="IA Soccer Analyse Pro", layout="wide")

# Estilo visual customizado
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
        .css-1d391kg {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Menu lateral com categorias
with st.sidebar:
    selected = option_menu("IA Soccer Analyse Pro", [
        "Dashboard",
        "Jogadores",
        "Sessão de Teste",
        "Testes Técnicos",
        "Análises Avançadas",
        "Relatórios"
    ], 
    icons=['bar-chart', 'person-lines-fill', 'calendar2-check', 'dribbble', 'cpu', 'file-earmark-text'], 
    menu_icon="cast", default_index=0)

# Conteúdo de cada aba
if selected == "Dashboard":
    st.title("📊 Dashboard")
    st.markdown("Resumo geral das avaliações técnicas da IA Soccer")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Players", "25", "+5%")
    col2.metric("Tests Completed", "58", "+10%")
    col3.metric("Average Score", "8.1", "+0.2")
    col4.metric("Reports Generated", "45", "+12")

elif selected == "Jogadores":
    st.title("👥 Gestão de Jogadores")
    st.markdown("Visualize e edite os dados dos jogadores registrados.")

elif selected == "Sessão de Teste":
    st.title("📝 Sessão de Teste")
    st.markdown("Crie e gerencie sessões de testes técnicas.")

elif selected == "Testes Técnicos":
    st.title("⚽ Testes Técnicos")
    teste = st.selectbox("Escolha o teste técnico", ["Teste Condução (Illinois)", "Teste de Passe", "Remate", "Sprint", "Agilidade", "Controle"])
    st.write(f"Você escolheu: **{teste}**")

elif selected == "Análises Avançadas":
    st.title("🧠 Análises Avançadas")
    st.markdown("Biomecânica, avaliação cognitiva, risco de lesão e outros dados técnicos.")

elif selected == "Relatórios":
    st.title("📄 Relatórios")
    st.markdown("Relatórios detalhados de desempenho por jogador ou por sessão.")
