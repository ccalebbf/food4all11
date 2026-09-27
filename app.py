import streamlit as st
from ZODB import DB
from ZODB.FileStorage import FileStorage

from sync import data_to_db

st.set_page_config(page_title="Food Distribution Database", layout="wide")
st.title("📦 Food Distribution Tracker")

st.text("Welcome to Food 4 All!")
st.text("This is a centralised databased aiming to coordinating food aid efforts in the Pearl Garden neighbourhood (Bedok North Ave 4), with an aim to reduce food wastage and increase efficiency.")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/food_dist_bags.jpeg", caption = "Food distributed at Block 106", width = 400)


if st.button("Sync Latest Data"):
    with st.spinner("Syncing Data..."):
        data_to_db()
        st.success("Sync Complete!")

if st.button("Click Button"):
    st.success("Nice Work!")