import streamlit as st
from google_sheets import add_deletion_records
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

# -- Defines Home Page --
st.set_page_config(page_title="Food Distribution Database", layout="wide")

try:
    data_to_db('Pearl Garden', pearl_garden)
except Exception as e:
    st.error(f"Sync failed on startup: {e}")

# -- Define Pages --
home_page = st.Page("pages/home.py", title = "Home", icon = '🏠', default = True)
#pg_page = st.Page("pages/pearl_garden.py", title = "Pearl Garden Neighbourhood Records", icon = '🏘️')
indi_page = st.Page("pages/block_records.py", title = "Block Records", icon = "🏡")
gp = st.Page("scrapped_pages/guinea_pig.py", title = 'Print Debugging', icon = "🧪")

## -- Page Navigator --
nav = st.navigation([home_page, indi_page, gp])
nav.run()
