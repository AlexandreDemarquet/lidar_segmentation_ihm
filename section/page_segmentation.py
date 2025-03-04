import streamlit as st
import requests
import numpy as np
import laspy
import tempfile
import os
import io
import zipfile


def build_page_segmentation():

    
    url = st.secrets["API_URL"]
    def load_laz_file(uploaded_file):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".laz") as tmpfile:
            tmpfile.write(uploaded_file.getvalue())
            tmpfile_path = tmpfile.name
    
        las = laspy.read(tmpfile_path)
        coords = np.vstack((las.x, las.y, las.z)).T  # Extraction des coordonnées X, Y, Z
        
        os.remove(tmpfile_path)
        
        return las, coords
    
    def classify_points(uploaded_file):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".laz") as tmpfile:
            tmpfile.write(uploaded_file.getvalue())
            tmpfile_path = tmpfile.name
    
        headers = {
            "Authorization": f"Bearer {api_key_enter}"
        }
        try:
            with open(tmpfile_path, "rb") as f:
                files = {"file": f}
                response = requests.post(url, files=files, headers=headers)
                
            
            os.remove(tmpfile_path)
            
            if response.status_code == 200:
                return np.array(response.json()["segmentation"], dtype=int)
    
            else:
                st.error("Erreur lors de la classification : " + response.text)
                return None
        except :
            st.error("Erreur d'API (clé ou service)")
            return None
    
    
    def save_classified_file(las, classes):
        las.classification = classes
        with tempfile.NamedTemporaryFile(delete=False, suffix=".laz") as tmpfile:
            las.write(tmpfile.name)
            return tmpfile.name
    
    
    st.title("Segmentation de Points LiDAR")
    st.write("Téléchargez des fichiers .laz/.las pour les classifier.")
    
    
    if "processed_files" not in st.session_state:
        st.session_state["processed_files"] = {}
    
    left, right = st.columns(2)   
    
    with left:
        api_key_enter = st.text_input("Votre clé d'API:")
    
        uploaded_files = st.file_uploader("Choisir des fichiers .las/.laz", type=["laz", "las"], accept_multiple_files=True)
        if uploaded_files:
            st.success(f"{len(uploaded_files)} fichier(s) téléchargé(s) avec succès!")
            progress_bar = st.progress(0)
            nb_file = len(uploaded_files)
            uploaded_files_copy = uploaded_files.copy()
            for i, uploaded_file in enumerate(uploaded_files_copy):
                if uploaded_file.name not in st.session_state["processed_files"].keys():
                    with st.spinner(f"Traitement du fichier {uploaded_file.name}..."):
                        las, coords = load_laz_file(uploaded_file)
                        classes = classify_points(uploaded_file)
    
                        if classes is not None:
                            classified_file = save_classified_file(las, classes)
                            st.session_state["processed_files"][uploaded_file.name] = classified_file
                            st.success(f"Fichier {uploaded_file.name} traité!")
                        else:
                            st.error(f"Erreur lors de la classification de {uploaded_file.name}.")
    
                    progress_bar.progress((i + 1) / nb_file)
    
    with right:
        if st.session_state["processed_files"]:
            st.write("### Télécharger les fichiers classifiés :")
            
            for filename, filepath in st.session_state["processed_files"].items():
                with open(filepath, "rb") as f:
                    st.download_button(
                        label=f"Télécharger {filename}",
                        data=f,
                        file_name=f"classified_{filename}",
                        mime="application/octet-stream"
                    )
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".zip") as tmp_zip:
                with zipfile.ZipFile(tmp_zip.name, 'w') as zipf:
                    for filename, filepath in st.session_state["processed_files"].items():
                        zipf.write(filepath, arcname=f"classified_{filename}")
                zip_path = tmp_zip.name
            
            with open(zip_path, "rb") as f:
                st.download_button(
                    label="Télécharger tous les fichiers classifiés",
                    data=f,
                    file_name="classified_files.zip",
                    mime="application/zip"
                )