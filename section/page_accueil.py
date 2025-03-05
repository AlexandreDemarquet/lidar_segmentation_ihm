
import streamlit as st
def build_page_accueil():

    # En-tête de la page
    st.title("Bienvenue sur notre Plateforme de Segmentation de Nuages de Points LiDAR")
    st.markdown("---")

    st.header("Transformez vos Données LiDAR avec l'Intelligence Artificielle")
    st.write(
        """
        Notre plateforme utilise des techniques avancées de deep learning pour segmenter vos nuages de points LiDAR.
        Que vous soyez dans l'industrie de la construction, de l'ingénierie civile, ou de la cartographie,
        notre solution vous offre des résultats précis et rapides.
        """
    )

    # Avantages
    st.header("Pourquoi Nous Choisir ?")
    st.markdown(
        """
        - **Rapidité** : Obtenez des résultats en quelques secondes grâce à notre infrastructure optimisée.
        - **Facilité d'Utilisation** : Téléchargez simplement votre fichier `.laz` ou `.las` et laissez-nous faire le reste.
        """
    )

    # Comment ça Marche
    st.header("Comment ça Marche ?")
    st.markdown(
        """
        1. **Téléchargez** votre fichier LiDAR sur notre plateforme.
        2. **Lancez** la segmentation en un clic.
        3. **Visualisez** et **téléchargez** les résultats.
        """
    )

    # Appel à l'Action
    st.header("Prêt à Commencer ?")
    st.markdown(
        """
        [Essayez notre service dès maintenant](#) et découvrez comment nous pouvons transformer vos données LiDAR.
        """
    )

    # Pied de Page
    st.markdown("---")
    st.write("© 2025 Votre Entreprise. Tous droits réservés.")