import streamlit as st
from ZODB import DB
from ZODB.FileStorage import FileStorage

from sync import data_to_db

# -- Helper to load Database Data --
def load_db_data():
    try:
        storage = FileStorage('Data.fs', read_only = True)
        db = DB(storage)
        connection = db.open()
        db_root = connection.root()
        neighbourhood = db_root.get('neighbourhood')
        return connection, db, neighbourhood
    except Exception as e:
        st.error(f"Error accessing database: {e}")
        return None, None, None

# -- Syncs Data --
try:
    data_to_db()
except Exception as e:
    st.error(f"Sync failed: {e}")

# -- Defines Home Page --
st.set_page_config(page_title="Food Distribution Database", layout="wide")

# -- Define Pages --
home_page = st.Page("app.py", title = "Home", icon = '🏠', default = True)
pg_page = st.Page("pages/1_pg.py", title = "Pearl Garden Neighbourhood Records", icon = '🏘️')

## -- Page Navigator --
nav = st.navigation({"Home": [home_page], "Pearl Garden Neighbourhood": [pg_page]})
nav.run()

st.header("Food 4 All")
st.text("Welcome! This is a centralised database aiming to coordinating food aid efforts in the Pearl Garden neighbourhood (Bedok North Ave 4), with an aim to reduce food wastage and increase efficiency.")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/food_dist_bags.jpeg", width = 400)

l1, c1, c2, c3, r1 = st.columns([1, 2, 2, 2, 1])

with c1:
    st.link_button("Log a Distribution!", 'https://docs.google.com/forms/d/1ROgMh8lEaYwNiOAIj8Bk-6-2HcLLsVgAtl5_oKXsQzA/')
with c2:
    st.link_button("Google Sheet of Distributions", 'https://docs.google.com/spreadsheets/d/1SuHBT_VcTySORDLElq1XTv3VRwXIOijrekMGioCqxzc/edit?resourcekey=&gid=1793904774#gid=1793904774')
with c3:
    if st.button("Refresh Latest Data"):
        try:
            data_to_db()
        except Exception as e:
            st.error(f"Sync failed: {e}")