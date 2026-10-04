# -- Page for Summarised Pearl Garden neighbourhood records --

import streamlit as st
from sync_updated import data_to_db

pearl_garden = {98: [460098, [1.334225, 103.939826]], 
                99: [460099, [1.333908, 103.939446]] , 
                100: [460100, [1.334289, 103.938856]], 
                101: [460101, [1.334461, 103.937938]], 
                102: [460102, [1.333882, 103.937461]], 
                103: [460103, [1.333458, 103.937525]], 
                104: [460104, [1.333297, 103.936613]], 
                105: [460105, [1.333705, 103.936565]], 
                106: [460106, [1.334439, 103.937123]]}
                
neighbourhood = data_to_db('Pearl Garden', pearl_garden)

if neighbourhood:

    st.title(f"Summary of {neighbourhood.name} Records")
    
    for block in neighbourhood.blocks:

        if block.latest_distribution is None:
            ld = "No Record"
            pd = 0
        else:
            ld = block.latest_distribution
            pd = len(block.distributions) - 1

        st.header(f"Block {block.block}")

        st.subheader("Latest Distribution 📦")

        st.text(f"{ld}")

        st.subheader("Days Since Latest Distribution 🗓️")

        st.text(f"{block.time_since_last_distribution()}")

        st.subheader("Number of Past Distributions 📖")

        st.text(f"{pd}")

if st.sidebar.button("🔄 Fetch Fresh Data"):
    st.cache_data.clear()
    st.rerun()