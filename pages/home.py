import streamlit as st
from app import data_to_db, load_db_data

st.header("🍚🍜🥬🥕🥦🫑 --- Food 4 All! --- 🌽🍎🍌🍊🍋🍞")
st.text("Welcome! This is a centralised database aiming to coordinating food aid efforts in the Pearl Garden neighbourhood (Bedok North Ave 4), with an aim to reduce food wastage and increase efficiency.")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/dist_bags.jpeg", width = 'stretch')


st.header("Log a Distribution Here!")
st.link_button("Google Form Link", 'https://docs.google.com/forms/d/1ROgMh8lEaYwNiOAIj8Bk-6-2HcLLsVgAtl5_oKXsQzA/')