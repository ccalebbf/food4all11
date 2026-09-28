import streamlit as st
from app import data_to_db, load_db_data

connection, db, neighbourhood = load_db_data()

st.set_page_config(page_title=f"Neighbourhood Records of {neighbourhood.name}", layout="wide")

if neighbourhood:
    st.text("Overall Blocks Records")
    for block in neighbourhood.blocks:
        st.text(f"{block}")