import streamlit as st
from app import data_to_db, load_db_data

st.markdown(
    """
    <style>
    button[data-baseweb="tab"] {
        margin: 0 auto;
        width: 100%;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

connection, db, neighbourhood = load_db_data()

#selected_view = st.radio("Navigation", ["View A", "View B", "View C"])

tab_labels = [f"Block {block.block}" for block in neighbourhood.blocks]

tabs = st.tabs(tab_labels)

#for tab, block in zip(tabs, neighbourhood.blocks):
