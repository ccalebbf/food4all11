import gspread
import streamlit as st
import transaction
from datetime import datetime, date
from ZODB import DB
from ZODB.FileStorage import FileStorage
from persistent.list import PersistentList

from db import load_db_data
from models import Distribution, Block, Neighbourhood

def get_gspread_client():
    if "gcp_service_account" in st.secrets:
        try:
            creds_dict = dict(st.secrets["gcp_service_account"])
            if "private_key" in creds_dict:
                creds_dict["private_key"] = creds_dict["private_key"].replace("\\n", "\n")
            return gspread.service_account_from_dict(creds_dict)
        except Exception as e:
            print(f"Failed to load, {e}")
    return gspread.service_account(filename = 'food_for_all.json')

@st.cache_data(ttl=300)
def fetch_google_sheet_records():
    gc = get_gspread_client()
    spreadsheet = gc.open("Food Distribution Logging Form (Responses)").sheet1
    return spreadsheet.get_all_records(numericise_ignore=['all'])

def data_to_db(connection = None):

    if connection is None:
        connection, _, _ = load_db_data()

    if connection is None:
        st.sidebar.error("❌ Sync Error: No DB connection available.")
        print("[SYNC ERROR] No DB connection available.")
        return

    print("\n--- Starting sync.py data_to_db() ---")
    st.sidebar.info("🔄 Running sync from Google Sheets...")

    try:
        all_rows = fetch_google_sheet_records()
        print(f"[SYNC LOG] Fetched {len(all_rows)} rows from Google Sheets.")
    except Exception as e:
        st.sidebar.error(f"❌ Sheet fetch error: {e}")
        print(f"[SYNC ERROR] Sheet fetch error: {e}")
        return

    db_root = connection.root()

    pearl_garden = {98: 460098, 99: 460099, 
                100: 460100, 101: 460101, 
                102: 460102, 103: 460103, 
                104: 460104, 105: 460105, 
                106: 460106}

    if 'neighbourhood' not in db_root:
        print("[SYNC LOG] 'neighbourhood' missing from db_root. Creating new instance...")
        pg = Neighbourhood('Pearl Garden', [Block(key, pearl_garden[key]) for key in pearl_garden])
        db_root['neighbourhood'] = pg
        transaction.commit()
    
    n = db_root['neighbourhood']

    for row in all_rows:

        blocks_covered = [int(x.strip()) for x in row['Blocks Covered'].split(",")]

        dist_id = datetime.strptime(row['Timestamp'], "%m/%d/%Y %H:%M:%S").strftime("%y%m%d%H%M%S")

        for block in n.blocks:
            
            if block.block in blocks_covered:
                
                existing_ids = PersistentList(d for d in block.distributions)

                if dist_id not in block.deleted_distributions and dist_id not in existing_ids:
                    new_dist = Distribution(row['Name of organisation'], 
                                            row['Date of distribution'], 
                                            row['Type of Food distributed'], 
                                            row['Number of people catered to (estimate)'], 
                                            row['Were the food distributed halal certified?'])
                    block.log_distribution(dist_id, new_dist)

    transaction.commit()
    connection.sync()

    print(f"[SYNC LOG] Sync complete. Added new distribution(s).")