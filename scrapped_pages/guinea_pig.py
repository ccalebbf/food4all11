import streamlit as st
import folium
from streamlit_folium import st_folium
from sync_updated import data_to_db
from map import time_to_colour


st.markdown(
    """
    <div style="background-color: #0066cc; color: white; padding: 15px; border-radius: 8px;">
        <strong>Custom Block:</strong> This is a text block with a custom blue background and white text.
    </div>
    """,
    unsafe_allow_html=True
)