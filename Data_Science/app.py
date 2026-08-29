import streamlit as st
from pages import home, grammar_fun, reading_translation

st.set_page_config(
    page_title="Data Science Fun & Learn",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

PAGES = {
    "Home": home,
    "MCQ Generator": grammar_fun,
    "SQL Explainer": reading_translation
}

def main():
    st.sidebar.title("Navigation")

    selection = st.sidebar.radio(
        "Go to",
        list(PAGES.keys())
    )

    PAGES[selection].app()

if __name__ == "__main__":
    main()