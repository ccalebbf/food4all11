import streamlit as st
from app import data_to_db, load_db_data

connection, db, neighbourhood = load_db_data()

if neighbourhood:
    
    for block in neighbourhood:
        
        sorted_distributions = dict(sorted(self.distributions.items(), key = lambda item: item[1].date))

        block_data = {
            "Distribution ID" : [key for key in sorted_distributions],
            "Date" : [value.date for value in sorted_distributions.values()],
            "Organisation" : [value.org for value in sorted_distributions.values()],
            "Type" : [value.type for value in sorted_distributions.values()],
            "Number of People (Approx.)" : [value.pax for value in sorted_distributions.values()],
            "Halal-Certified" : [value.isHalal for value in sorted_distributions.values()]
        }

        st.table(block_data, border="horizontal")