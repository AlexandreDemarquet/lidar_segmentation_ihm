import streamlit as st
from section.page_connection import build_page_connection
from section.page_accueil import build_page_accueil
from section.page_segmentation import build_page_segmentation
def main():
    st.set_page_config(
        page_title="Segmentation de Nuages de Points LiDAR",
        page_icon="🌐",
        layout="wide"
    )

    st.sidebar.title("Navigation")


    selection_page="accueil"
    if st.sidebar.button("Accueil"):
        selection_page="accueil"

    if st.sidebar.button("Accéder à l'Espace Client"):
        if "authenticated" not in st.session_state:
            selection_page = "connection"
        else:
            selection_page = "segmentation"
    
    if st.sidebar.button("Voir les Tarifs"):
        selection_page = "tarif"
    if st.sidebar.button("Créer un Compte"):
        selection_page = "creation_compte"

    if st.sidebar.button("Contactez-Nous"):
        selection_page = "contact"

    match selection_page:
        case "accueil":
            build_page_accueil()
        case "connection":
            build_page_connection()
            if "authenticated" in st.session_state:
                build_page_segmentation()


        case "tarif":
            pass
        case "creation_compte":
            pass
        case "contact":
            pass
        case "segmentation":
            build_page_segmentation()
    
    

if __name__ == "__main__":
    main()
