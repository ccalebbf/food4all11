import streamlit as st
from ZODB import DB
from ZODB.FileStorage import FileStorage

st.set_page_config(page_title="Food Distribution Dashboard", layout="wide")
st.title("📦 Food Distribution Tracker")
