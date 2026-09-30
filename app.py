import streamlit as st
import transaction
from ZODB import DB
from ZODB.FileStorage import FileStorage

from sync import data_to_db


@st.cache_resource
def get_db_connection():
    try:
        storage = FileStorage('Data.fs')
        db = DB(storage)
        connection = db.open()
    except Exception as e:
        st.error(f"Error opening database: {e}")
        return None, None

# -- Helper to load Database Data --
def load_db_data():
    db, connection = get_db_connection()
    if connection is None:
        return None, None, None
    try:
        connection.sync()
        db_root = connection.root()
        neighbourhood = db_root.get('neighbourhood')

        if neighbourhood is None:
            connection.sync()
            neighbourhood = db_root.get('neighbourhood')

        return connection, db, neighbourhood
    except Exception as e:
        st.error(f"Error accessing database: {e}")
        return connection, db, None

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
indi_page = st.Page("pages/indiv.py", title = "Individual Block Records", icon = "🏡")

## -- Page Navigator --
nav = st.navigation([home_page, pg_page, indi_page])
nav.run()