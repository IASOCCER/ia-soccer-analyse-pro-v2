import streamlit as st

st.set_page_config(page_title="IA Soccer Analyse Pro", layout="wide")

# ----- MENU LATERAL -----
menu = st.sidebar.selectbox("Sélectionnez une section", [
    "🏠 Accueil",
    "📊 Passe",
    "⚽ Tir",
    "🏃 Sprint",
    "🧠 Réaction",
    "🧭 Agilité",
    "🧍 Masse musculaire",
    "🔬 Biomecanique vidéo",
    "📝 Rapport Global"
])

# ----- FUNÇÕES PARA CADA MÓDULO (simples placeholders por enquanto) -----
def page_accueil():
    st.title("Rapports et Documentation")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("📄 Rapports Individuels")
        st.markdown("""
        - Profil technique complet  
        - Comparaison avec standards académies  
        - Recommandations personnalisées  
        - Évolution temporelle  
        """)
        st.markdown("✍️ **Générer (Bientôt)**")
    with col2:
        st.subheader("📘 Rapports de Session")
        st.markdown("""
        - Résultats détaillés par test  
        - Conditions d'évaluation  
        - Photos et vidéos  
        - Notes de l'entraîneur  
        """)
        st.markdown("🛠️ **Exporter (Développement)**")
    with col3:
        st.subheader("👥 Rapports d'Équipe")
        st.markdown("""
        - Statistiques d'équipe  
        - Benchmarks collectifs  
        - Forces/faiblesses  
        - Plans d'entraînement  
        """)
        st.markdown("🔒 **Partager (Futur)**")

    st.markdown("---")
    st.subheader("Fonctionnalités Actuellement Disponibles")
    col4, col5 = st.columns(2)
    with col4:
        st.success("✅ Tests Professionnels")
        st.markdown("""
        - La Masia  
        - Ajax TIPS  
        - Real Madrid La Fábrica  
        - Comparaisons par âge
        """)
    with col5:
        st.success("✅ Ressources Vidéo")
        st.markdown("""
        - Tutoriels des académies  
        - Vidéos techniques  
        - Protocoles officiels
        """)

def page_passe():
    st.title("Analyse de Passe")
    st.markdown("🔍 Module pour enregistrer et analyser les passes avec IA.")

def page_tir():
    st.title("Analyse de Tir")
    st.markdown("⚽ Enregistrez la puissance et la précision des tirs.")

def page_sprint():
    st.title("Analyse de Sprint")
    st.markdown("🏃 Chronométrez les sprints sur 10m et 20m avec comparaisons par âge.")

def page_reaction():
    st.title("Test de Réaction")
    st.markdown("🧠 Mesure du temps de réaction à stimulus visuel ou auditif.")

def page_agilite():
    st.title("Test d’Agilité")
    st.markdown("🧭 Illinois ou Zigzag, avec ou sans ballon.")

def page_masse():
    st.title("Analyse corporelle")
    st.markdown("🧍 Résultats de la balance intelligente (masse musculaire, graisse, IMC...).")

def page_biomeca():
    st.title("Analyse biomécanique par vidéo")
    st.markdown("🔬 Téléverser une vidéo et obtenir feedback sur la posture et le mouvement.")

def page_rapport():
    st.title("Rapport Global")
    st.markdown("📝 Synthèse des résultats, recommandations IA, et génération PDF.")

# ----- ROTEADOR -----
if menu == "🏠 Accueil":
    page_accueil()
elif menu == "📊 Passe":
    page_passe()
elif menu == "⚽ Tir":
    page_tir()
elif menu == "🏃 Sprint":
    page_sprint()
elif menu == "🧠 Réaction":
    page_reaction()
elif menu == "🧭 Agilité":
    page_agilite()
elif menu == "🧍 Masse musculaire":
    page_masse()
elif menu == "🔬 Biomecanique vidéo":
    page_biomeca()
elif menu == "📝 Rapport Global":
    page_rapport()
