import streamlit as st
from PIL import Image
import hmac


### CONFIGURATION PAGE
im = Image.open('./image/App_Icon.webp')
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    page_title="LIDAR automatique segmentation",
    page_icon=im)




def build_page():
    st.switch_page("./pages/Segmentation_Automatique.py")


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            # del st.session_state["username"]
            st.session_state["authenticated_user"] = st.session_state["username"]  # Stockez le nom d'utilisateur
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password() and "authenticated" not in st.session_state:
    st.stop()
else:
    st.session_state["authenticated"] = True 
    build_page()
