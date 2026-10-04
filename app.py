import streamlit as st
from google_sheets import add_deletion_records
from sync_updated import data_to_db

pearl_garden = {98: 460098, 99: 460099, 
                100: 460100, 101: 460101, 
                102: 460102, 103: 460103, 
                104: 460104, 105: 460105, 
                106: 460106}

# -- Defines Home Page --
st.set_page_config(page_title="Food Distribution Database", layout="wide")

try:
    data_to_db('Pearl Garden', pearl_garden)
except Exception as e:
    st.error(f"Sync failed on startup: {e}")

# -- Define Pages --
home_page = st.Page("pages/home.py", title = "Home", icon = '🏠', default = True)
pg_page = st.Page("pages/pearl_garden.py", title = "Pearl Garden Neighbourhood Records", icon = '🏘️')
indi_page = st.Page("pages/block_records.py", title = "Block Records", icon = "🏡")
gp = st.Page("pages/guinea_pig.py", title = 'Print Debugging', icon = "🧪")

## -- Page Navigator --
nav = st.navigation([home_page, pg_page, indi_page, gp])
nav.run()
