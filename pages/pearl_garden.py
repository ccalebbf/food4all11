import streamlit as st
from sync_updated import data_to_db

pearl_garden = {98: [460098, [1.33429725783725, 103.93986643128832]], 
                99: [460099, [1.333887121833775, 103.9394561840746]] , 
                100: [460100, [1.3343449481580134, 103.93880989153601]], 
                101: [460101, [1.3344575703838415, 103.93783893187799]], 
                102: [460102, [1.333894459203151, 103.93740977843797]], 
                103: [460103, [1.33346542202661, 103.93753852446999]], 
                104: [460104, [1.3332348145085486, 103.93646027644773]], 
                105: [460105, [1.3336370369014425, 103.93650855620973]], 
                106: [460106, [1.334420029637709, 103.93705572684574]]}

neighbourhood = data_to_db('Pearl Garden', pearl_garden)

if neighbourhood:

    st.title(f"Summary of {neighbourhood.name} Records")
    
    for block in neighbourhood.blocks:
        
        st.write(block.coordinates)
        
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