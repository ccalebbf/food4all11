import streamlit as st
from ZODB import DB
from ZODB.FileStorage import FileStorage

from sync import data_to_db

# -- Helper to get Database Data --
@st.cache_resource
def get_db_connection():
    try:
        storage = FileStorage('Data.fs')
        db = DB(storage)
        connection = db.open()
        return db, connection
    except Exception as e:
        st.error(f"Error accessing database: {e}")
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
            conection.sync()
            neighbourhood = db_root.get('neighbourhood')      
        return connection, db, neighbourhood
    except Exception as e:
        st.error(f"Error reading from database: {e}")
        return connection, db, None

# -- Defines Home Page --
st.set_page_config(page_title="Food Distribution Database", layout="wide")

# -- Syncs Data --
connection, db, neighbourhood = load_db_data()
if connection:
    try:
        data_to_db(connection)
    except Exception as e:
        st.error(f"Sync failed: {e}")

# -- Define Pages --
home_page = st.Page("pages/home.py", title = "Home", icon = '🏠', default = True)
pg_page = st.Page("pages/pg.py", title = "Pearl Garden Neighbourhood Records", icon = '🏘️')
indi_page = st.Page("pages/indiv.py", title = "Individual Block Records", icon = "🏡")

## -- Page Navigator --
nav = st.navigation([home_page, pg_page, indi_page])
nav.run()