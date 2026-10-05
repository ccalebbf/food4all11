import streamlit as st
import folium
from streamlit_folium import st_folium
from sync_updated import data_to_db
from map import time_to_colour


st.markdown(
    """
    <div style="background-color: #c412bd; color: white; padding: 15px; border-radius: 8px;">
        <strong>Within 1 week</strong>
    </div>
    """,
    unsafe_allow_html=True
)