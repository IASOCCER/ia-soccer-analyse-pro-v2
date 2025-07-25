import streamlit as st
import pandas as pd
import datetime

# --- CONFIGURAÇÃO GERAL ---
st.set_page_config(page_title="IA Soccer Analyse Pro", layout="wide")

# --- MENU LATERAL ---
menu = st.sidebar.selectbox("Navegação", [
    "🏠 Dashboard", 
    "👥 Jogadores", 
    "🧪 Sessão de Teste", 
    "📊 Teste Illinois",
    "📄 Relatórios"
])

# --- BANCO DE DADOS FICTÍCIO PARA COMPARAÇÃO ---
tabela_referencia = {
    'U8': 21.5,
    'U10': 19.5,
    'U12': 18.0,
    'U14': 17.3,
    'U16': 16.5,
    'U18': 16.0,
    'Sénior': 15.8
}

# --- FUNÇÃO DE ANÁLISE ---
def analisar_ilinois(tempo, idade):
    if idade <= 8:
        ref = tabela_referencia['U8']
    elif idade <= 10:
        ref = tabela_referencia['U10']
    elif idade <= 12:
        ref = tabela_referencia['U12']
    elif idade <= 14:
        ref = tabela_referencia['U14']
    elif idade <= 16:
        ref = tabela_referencia['U16']
    elif idade <= 18:
        ref = tabela_referencia['U18']
    else:
        ref = tabela_referencia['Sénior']

    diferenca = tempo - ref

    if tempo <= ref:
        nivel = "Elite"
    elif tempo <= ref + 0.3:
        nivel = "Muito Bom"
    elif tempo <= ref + 0.5:
        nivel = "Bom"
    elif tempo <= ref + 0.8:
        nivel = "Médio"
    else:
        nivel = "A Melhorar"

    return nivel, ref, diferenca

# --- PLANO DE AÇÃO ---
def plano_de_acao(nivel):
    if nivel == "Elite":
        return "Manutenção do desempenho com foco em prevenção de lesões e mobilidade."
    elif nivel == "Muito Bom":
        return "Aprimorar saídas de mudança de direção e reação com estímulos visuais."
    elif nivel == "Bom":
        return "Trabalhar explosão inicial e agilidade com circuitos curtos e treino de frenagem."
    elif nivel == "Médio":
        return "Melhorar o controle corporal e tempo de reação em mudanças de direção."
    else:
        return "Plano intensivo de 8 semanas focado em coordenação, resistência e velocidade lateral."

# --- PÁGINAS ---
if menu == "🏠 Dashboard":
    st.title("📊 IA Soccer Analyse Pro")
    st.subheader("Bem-vindo ao sistema de avaliação técnica e física dos atletas IA Soccer.")
    st.markdown("---")
    st.info("Utilize o menu lateral para navegar pelos testes e análises.")

elif menu == "👥 Jogadores":
    st.title("👥 Registro de Jogadores")
    with st.form("form_jogador"):
        nome = st.text_input("Nome completo")
        idade = st.number_input("Idade", 6, 25)
        posicao = st.selectbox("Posição", ["Zagueiro", "Meio-campista", "Atacante", "Goleiro"])
        submit = st.form_submit_button("Registrar")
        if submit:
            st.success(f"Jogador {nome} registrado com sucesso!")

elif menu == "🧪 Sessão de Teste":
    st.title("🧪 Sessão de Testes Técnicos")
    st.warning("Página em desenvolvimento. Em breve, você poderá registrar todos os testes em sequência.")

elif menu == "📊 Teste Illinois":
    st.title("📊 Teste de Agilidade - Illinois")
    with st.form("form_ilinois"):
        nome = st.text_input("Nome do Atleta")
        idade = st.number_input("Idade do Atleta", 6, 25)
        tempo = st.number_input("Tempo do teste (segundos)", 10.0, 30.0, step=0.01)
        testar = st.form_submit_button("Analisar Desempenho")

    if testar:
        nivel, ref, diff = analisar_ilinois(tempo, idade)
        plano = plano_de_acao(nivel)

        st.success(f"Resultado: {nivel}")
        st.metric("Tempo Obtido", f"{tempo:.2f}s")
        st.metric("Tempo de Referência", f"{ref:.2f}s")
        st.metric("Diferença", f"{diff:+.2f}s")

        st.markdown("---")
        st.subheader("📈 Comparação com Academias Profissionais")
        st.markdown("""
        | Categoria | Tempo Elite |
        |-----------|--------------|
        | U8        | 21.5s        |
        | U10       | 19.5s        |
        | U12       | 18.0s        |
        | U14       | 17.3s        |
        | U16       | 16.5s        |
        | U18       | 16.0s        |
        | Sénior    | 15.8s        |
        """)

        st.markdown("---")
        st.subheader("📋 Plano de Ação Personalizado")
        st.info(plano)

elif menu == "📄 Relatórios":
    st.title("📄 Relatórios e Evolução do Atleta")
    st.warning("Módulo de relatórios será ativado após os primeiros testes.")

