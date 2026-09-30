import streamlit as st
from app import data_to_db, load_db_data
from ZODB import DB
from ZODB.FileStorage import FileStorage

connection, db, neighbourhood = load_db_data()

st.header(f"Overall Records of {neighbourhood.name}")

if neighbourhood:
    for block in neighbourhood.blocks:
        st.text(f"{block}")

if st.button("Refresh Latest Data"):
    try:
        data_to_db(connection)
    except Exception as e:
        st.error(f"Sync failed: {e}")
