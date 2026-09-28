import streamlit as st
from app import data_to_db, load_db_data

st.header("Food 4 All")
st.text("Welcome! This is a centralised database aiming to coordinating food aid efforts in the Pearl Garden neighbourhood (Bedok North Ave 4), with an aim to reduce food wastage and increase efficiency.")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/food_dist_bags.jpeg", width = 400)

st.link_button("Log a Distribution!", 'https://docs.google.com/forms/d/1ROgMh8lEaYwNiOAIj8Bk-6-2HcLLsVgAtl5_oKXsQzA/')

st.link_button("Google Sheet of Distributions", 'https://docs.google.com/spreadsheets/d/1SuHBT_VcTySORDLElq1XTv3VRwXIOijrekMGioCqxzc/edit?resourcekey=&gid=1793904774#gid=1793904774')

if st.button("Refresh Latest Data"):
    try:
        data_to_db()
    except Exception as e:
        st.error(f"Sync failed: {e}")