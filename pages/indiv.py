import streamlit as st
from streamlit_option_menu import option_menu
from app import data_to_db, load_db_data

connection, db, neighbourhood = load_db_data()

#selected_view = st.radio("Navigation", ["View A", "View B", "View C"])

selected = option_menu(menu_title = "Pick a Block", options = [block.block for block in neighbourhood.blocks])