import streamlit as st
from db import load_db_data
from sync_updated import data_to_db

# -- Defines Home Page --
st.set_page_config(page_title="Food Distribution Database", layout="wide")

connection, db, neighbourhood = load_db_data()

if connection:
    try:
        data_to_db(connection)
        connection.sync()
        neighbourhood = connection.root().get('neighbourhood')
    except Exception as e:
        st.error(f"Sync failed on startup: {e}")


# -- Define Pages --
home_page = st.Page("pages/home.py", title = "Home", icon = '🏠', default = True)
pg_page = st.Page("pages/pg.py", title = "Pearl Garden Neighbourhood Records", icon = '🏘️')
indi_page = st.Page("pages/indiv.py", title = "Individual Block Records", icon = "🏡")

## -- Page Navigator --
nav = st.navigation([home_page, pg_page, indi_page])
nav.run()

