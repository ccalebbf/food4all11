import streamlit as st
import folium
from streamlit_folium import st_folium
from sync_updated import data_to_db
from map import time_to_colour


st.markdown("This text has a :red[red colored word] inside it.")
st.markdown(":blue[This entire sentence is blue.]")