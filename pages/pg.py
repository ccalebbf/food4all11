import streamlit as st
from app import data_to_db, load_db_data
from ZODB import DB
from ZODB.FileStorage import FileStorage


connection, db, neighbourhood = load_db_data()

st.header(f"Overall Records of {neighbourhood.name}")

if neighbourhood:
    
    for block in neighbourhood.blocks:

        # st.text(f"{block}") 

        if block.latest_distribution is None:
            ld = "No Record"
            pd = 0
        else:
            ld = block.latest_distribution
            pd = len(block.distributions) - 1

        st.header(f"Block {block.block}")

        st.subheader("Latest Distribution ")

        st.text(f"{ld}")

        st.subheader(f"Days Since Latest Distribution: {block.time_since_last_distribution()}")

        st.subheader(f"Number of Past Distributions: {pd}")

if st.button("Refresh Latest Data"):
    try:
        data_to_db()
    except Exception as e:
        st.error(f"Sync failed: {e}")
