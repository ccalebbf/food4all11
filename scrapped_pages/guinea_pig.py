import streamlit as st
import folium
from streamlit_folium import st_folium
from sync_updated import data_to_db
from map import time_to_colour


st.markdown(":violet[No Record]")
st.markdown(":blue[Within 1 week]")
st.markdown(":green[Between 1 to 2 weeks]")
st.markdown(":orange[Between 2 to 4 weeks]")
st.markdown(":red[Over 4 weeks]")