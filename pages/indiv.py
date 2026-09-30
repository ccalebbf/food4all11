import streamlit as st
from app import data_to_db, load_db_data

connection, db, neighbourhood = load_db_data()

selected_view = st.radio("Navigation", ["View A", "View B", "View C"])
