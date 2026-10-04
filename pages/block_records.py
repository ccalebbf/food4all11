import streamlit as st
from google_sheets import add_deletion_records
from sync_updated import data_to_db

pearl_garden = {98: 460098, 99: 460099, 
                100: 460100, 101: 460101, 
                102: 460102, 103: 460103, 
                104: 460104, 105: 460105, 
                106: 460106}

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