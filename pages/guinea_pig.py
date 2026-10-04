import streamlit as st
import folium

from streamlit_folium import st_folium

m = folium.Map(location=[1.333733, 103.938066], zoom_start = 16)

st_data = st_folium(m, width=725)