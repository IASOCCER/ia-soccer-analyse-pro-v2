import streamlit as st

st.set_page_config(page_title="IA Soccer International", layout="wide")

st.markdown("<h1 style='text-align: center;'>Rapports et Documentation</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.success("### 📄 Rapports Individuels\n\n- Profil technique complet\n- Comparaison avec standards académies\n- Recommandations personnalisées\n- Évolution temporelle\n\n🚧 *Générer (Bientôt)*")

with col2:
    st.info("### 📘 Rapports de Session\n\n- Résultats détaillés par test\n- Conditions d'évaluation\n- Photos et vidéos\n- Notes de l'entraîneur\n\n🔧 *Exporter (Développement)*")

with col3:
    st.warning("### 👥 Rapports d'Équipe\n\n- Statistiques d'équipe\n- Benchmarks collectifs\n- Forces/faiblesses\n- Plans d'entraînement\n\n🔒 *Partager (Futur)*")

st.markdown("---")
st.subheader("Fonctionnalités Actuellement Disponibles")

col4, col5 = st.columns(2)

with col4:
    st.success("#### ✅ Tests Professionnels\n- La Masia\n- Ajax TIPS\n- Real Madrid La Fábrica\n- Comparaisons par âge")

with col5:
    st.success("#### ✅ Ressources Vidéo\n- Tutoriels des académies\n- Vidéos techniques\n- Protocoles officiels")

st.markdown("<br><br>", unsafe_allow_html=True)
