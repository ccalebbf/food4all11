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

st.text("Legend (time since last distribution)")

cols = st.columns(5)

with cols[0]:
    #st.markdown("🟣 **No Record**")
    #st.markdown(":violet[No Record]")
    st.markdown(
    """
    <div style="background-color: #c412bd; color: white; padding: 15px; border-radius: 8px;">
        <strong>Within 1 week</strong>
    </div>
    """,
    unsafe_allow_html=True
    )

with cols[1]:
    #st.markdown("🔵 **Within 1 week**")
    #st.markdown(":blue[Within 1 week]")
    st.markdown(
    """
    <div style="background-color: #c412bd; color: white; padding: 15px; border-radius: 8px;">
        <strong>Within 1 week</strong>
    </div>
    """,
    unsafe_allow_html=True
    )
with cols[2]:
    #st.markdown("🟢 **Within 1 to 2 weeks**")
    #st.markdown(":green[Between 1 to 2 weeks]")
    st.markdown(
    """
    <div style="background-color: #c412bd; color: white; padding: 15px; border-radius: 8px;">
        <strong>Within 1 week</strong>
    </div>
    """,
    unsafe_allow_html=True
    )

with cols[3]:
    #st.markdown("🟠 **Within 2 to 4 weeks**")
    #st.markdown(":orange[Between 2 to 4 weeks]")
    st.markdown(
    """
    <div style="background-color: #c412bd; color: white; padding: 15px; border-radius: 8px;">
        <strong>Within 1 week</strong>
    </div>
    """,
    unsafe_allow_html=True
    )

with cols[4]:
    #st.markdown("🔴 **Over 4 weeks**")
    #st.markdown(":red[Over 4 weeks]")
    st.markdown(
    """
    <div style="background-color: #c412bd; color: white; padding: 15px; border-radius: 8px;">
        <strong>Within 1 week</strong>
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