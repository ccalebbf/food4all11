import streamlit as st
from app import data_to_db, load_db_data

connection, db, neighbourhood = load_db_data()

st.header(f"Overall Records of {neighbourhood.name}")

if neighbourhood:
    for block in neighbourhood.blocks:
        st.text(f"{block}")