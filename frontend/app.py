import streamlit as st

st.set_page_config(
    page_title="SilverWing",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("🍽️ SilverWing Dashboard")
st.markdown("Welcome to the admin interface for managing your dishes!")

st.info("Use the sidebar to navigate between pages:\n- **View Dishes**\n- **Dish Details**")
