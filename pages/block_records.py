# -- Page for Individual Block Records --

import streamlit as st
from google_sheets import get_gspread_client, add_deletion_records, sheets_clear_cache
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

st.title("Records of Individual Block")

tab_labels = [f"Block {block.block}" for block in neighbourhood.blocks]

tabs = st.tabs(tab_labels)

for tab, block in zip(tabs, neighbourhood.blocks):

    with tab:

        if neighbourhood:

            sorted_distributions = dict(sorted(block.distributions.items(), key = lambda item: item[1].date))

            st.header(f"Block {block.block}")
            
            block_data = {
                "Distribution ID" : [key for key in sorted_distributions],
                "Date" : [value.date for value in sorted_distributions.values()],
                "Organisation" : [value.org for value in sorted_distributions.values()],
                "Type" : [value.typ for value in sorted_distributions.values()],
                "Number of People (Approx.)" : [value.pax for value in sorted_distributions.values()],
                "Halal-Certified" : [value.isHalal for value in sorted_distributions.values()]
            }

            st.table(block_data, border="horizontal")

        with st.popover("Remove a Distribution"):

            removed_id = st.text_input("Enter Distribution ID: ", key=f"remove_id_{block.block}")

            if st.button("Confirm Removal", key=f"confirm_delete_btn_{block.block}"):

                if removed_id.strip():

                    res = block.rem_distribution(removed_id)

                    if res is not None:
                        add_deletion_records(block.block, removed_id)
                        st.success(f"Distribution {removed_id} removed!")
                        st.cache_data.clear()
                        data_to_db.clear()
                        st.rerun()
                    else:
                        st.error(f"Distribution (ID: {removed_id}) does not exist!")


if st.sidebar.button("🔄 Fetch Fresh Data"):
    st.cache_data.clear()
    st.rerun()