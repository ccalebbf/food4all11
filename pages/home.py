# -- Home Page --

import streamlit as st
from streamlit_folium import st_folium
from map import create_pg_map

st.title("Food 4 All! 🍚🍜🥬🥕🥦🫑🌽🍎🍌🍊🍋🍞")
st.text("Welcome! This is a centralised database aiming to coordinating food aid efforts in the Pearl Garden neighbourhood (Bedok North Ave 4), with an aim to reduce food wastage and increase efficiency.")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/dist_bags.jpeg", width = 'stretch')

st.header("Pearl Garden Neighbourhood Records")
m = create_pg_map()
st_data = st_folium(m, width=800, height=550, returned_objects = [])

st.header("Log a Distribution Here!")
st.text("Fill up this Google Form that will only take a minute!")
st.link_button("Google Form Link", 'https://docs.google.com/forms/d/1ROgMh8lEaYwNiOAIj8Bk-6-2HcLLsVgAtl5_oKXsQzA/')

