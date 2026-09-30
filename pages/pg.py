import streamlit as st
from app import data_to_db, load_db_data
from ZODB import DB
from ZODB.FileStorage import FileStorage


connection, db, neighbourhood = load_db_data()

if neighbourhood:

    st.title(f"Records of {neighbourhood.name}")
    
    for block in neighbourhood.blocks:

        if block.latest_distribution is None:
            ld = "No Record"
            pd = 0
        else:
            ld = block.latest_distribution
            pd = len(block.distributions) - 1

        st.header(f"Block {block.block}")

        st.subheader("Latest Distribution ")

        st.text(f"{ld}")

        st.subheader("Days Since Latest Distribution")

        st.text(f"{block.time_since_last_distribution()}")

        st.subheader("Number of Past Distributions")

        st.text(f"{ld}")

if st.button("Refresh Latest Data"):
    try:
        data_to_db()
    except Exception as e:
        st.error(f"Sync failed: {e}")
