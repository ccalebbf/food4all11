import streamlit as st
from ZODB import DB
from ZODB.FileStorage import FileStorage

st.set_page_config(page_title="Food Distribution Database", layout="wide")
st.title("📦 Food Distribution Tracker")

st.text("Welcome to Food 4 All! This is a centralised databased aiming to coordinating food aid efforts in the Pearl Garden neighbourhood (Bedok North Ave 4), with an aim to reduce food wastage and increase efficiency.")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("images/food_dist_bags.jpeg", caption = "Food distributed at Block 106", width = 400)