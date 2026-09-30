import streamlit as st
import transaction
from app import data_to_db, load_db_data

connection, db, neighbourhood = load_db_data()

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
                            transaction.commit()
                            if connection:
                                connection.sync()
                            st.success(f"Distribution {removed_id} removed")
                            st.rerun()
                        else:
                            st.error(f"Distribution {removed_id} does not Exist!")