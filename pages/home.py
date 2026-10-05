# -- Home Page --

import streamlit as st
from streamlit_folium import st_folium
from map import create_pg_map

st.title("Food 4 All! 🍚🍜🥬🥕🥦🫑🌽🍎🍌🍊🍋🍞")
st.text("Welcome! This is a centralised database aiming to coordinating food aid efforts in the Pearl Garden neighbourhood (Bedok North Ave 4), with an aim to reduce food wastage and increase efficiency.")

col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    st.image("images/dist_bags.jpeg", width = 'stretch')

st.subheader("Pearl Garden Neighbourhood Records")

st.text("Colour indicates time since last distribution")

cols = st.columns(5)

with cols[0]:
    st.markdown(
    """
    <div style="background-color: #c653b0; color: white; padding: 15px; border-radius: 8px;">
        <strong>No Record</strong>
    </div>
    """,
    unsafe_allow_html=True
    )

with cols[1]:
    st.markdown(
    """
    <div style="background-color: #31a3dc; color: white; padding: 15px; border-radius: 8px;">
        <strong>Within 1 week</strong>
    </div>
    """,
    unsafe_allow_html=True
    )
with cols[2]:
    st.markdown(
    """
    <div style="background-color: #68a922; color: white; padding: 15px; border-radius: 8px;">
        <strong>Between 1 to 2 weeks</strong>
    </div>
    """,
    unsafe_allow_html=True
    )

with cols[3]:
    st.markdown(
    """
    <div style="background-color: #f48c28; color: white; padding: 15px; border-radius: 8px;">
        <strong>Between 2 to 4 weeks</strong>
    </div>
    """,
    unsafe_allow_html=True
    )

with cols[4]:
    st.markdown(
    """
    <div style="background-color: #d63e2b; color: white; padding: 15px; border-radius: 8px;">
        <strong>Over 4 weeks</strong>
    </div>
    """,
    unsafe_allow_html=True
    )

st.write("")

c1, c2, c3 = st.columns([1, 8, 1])
with c2:
    m = create_pg_map()
    st_data = st_folium(m, width=850, height=550, returned_objects = [])

st.subheader("Log a Distribution Here!")
st.text("Fill up this Google Form that will only take a minute!")
st.link_button("Google Form Link", 'https://docs.google.com/forms/d/1ROgMh8lEaYwNiOAIj8Bk-6-2HcLLsVgAtl5_oKXsQzA/')

if st.sidebar.button("🔄 Fetch Fresh Data"):
    st.cache_data.clear()
    st.rerun()