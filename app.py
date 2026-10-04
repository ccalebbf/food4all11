import streamlit as st
from google_sheets import add_deletion_records
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
