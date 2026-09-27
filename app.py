import streamlit as st
from ZODB import DB
from ZODB.FileStorage import FileStorage

from sync import data_to_db

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

st.set_page_config(page_title="Food Distribution Database", layout="wide")
st.title("📦 Food Distribution Tracker")
st.header("Food 4 All")
st.text("Welcome! This is a centralised database aiming to coordinating food aid efforts in the Pearl Garden neighbourhood (Bedok North Ave 4), with an aim to reduce food wastage and increase efficiency.")

action = st.menu_button("Records", ['Overall Neighbourhood', 'Recent Distributions', 'By Block'])

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    st.image("images/food_dist_bags.jpeg", width = 400)

connection, db, neighbourhood = load_db_data()

if neighbourhood:
    st.text("Overall Blocks Records")
    for block in neighbourhood.blocks:
        st.text(f"{block}")


st.link_button("Log a Distribution!", 'https://docs.google.com/forms/d/1ROgMh8lEaYwNiOAIj8Bk-6-2HcLLsVgAtl5_oKXsQzA/')
st.link_button("Google Sheet of Distributions", 'https://docs.google.com/spreadsheets/d/1SuHBT_VcTySORDLElq1XTv3VRwXIOijrekMGioCqxzc/edit?resourcekey=&gid=1793904774#gid=1793904774')
if st.button("Refresh Latest Data"):
    try:
        data_to_db()
    except Exception as e:
        st.error(f"Sync failed: {e}")