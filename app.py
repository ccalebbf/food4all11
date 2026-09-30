import streamlit as st
from ZODB import DB
from ZODB.FileStorage import FileStorage

from sync import data_to_db

# -- Helper to load Database Data --
def load_db_data():
    try:
        storage = FileStorage('Data.fs')
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
home_page = st.Page("pages/home.py", title = "Home", icon = '🏠', default = True)
pg_page = st.Page("pages/pg.py", title = "Pearl Garden Neighbourhood Records", icon = '🏘️')

## -- Page Navigator --
nav = st.navigation([home_page, pg_page])
nav.run()