import streamlit as st
from google_sheets import get_gspread_client, add_deletion_records
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
                "Type" : [value.type for value in sorted_distributions.values()],
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
                        add_deletion_records(block, removed_id)
                        st.success(f"Distribution {removed_id} removed!")
                        st.rerun()
                    else:
                        st.error(f"Distribution (ID: {removed_id}) does not exist!")

if st.sidebar.button("🔄 Fetch Fresh Data"):
    st.cache_data.clear()
    st.rerun()