# -- File with all things related to syncing data --

import gspread
import streamlit as st
import time
from datetime import datetime, date
from models import Distribution, Block, Neighbourhood
from google_sheets import get_gspread_client, fetch_distribution_records, fetch_deletion_records

@st.cache_data(ttl=300, show_spinner = False)
def data_to_db(neighbourhood, blocks):
    
    pg = Neighbourhood(neighbourhood, [Block(key, blocks[key][0], blocks[key][1]) for key in blocks])
    
    gc = get_gspread_client()

    for block in pg.blocks:

        block.deleted_distributions = fetch_deletion_records(gc, block.block)

        time.sleep(1)

    try:
        all_rows = fetch_distribution_records(gc)
        print(f"[SYNC LOG] Fetched {len(all_rows)} rows from Google Sheets.")
    except Exception as e:
        st.sidebar.error(f"❌ Sheet fetch error: {e}")
        print(f"[SYNC ERROR] Sheet fetch error: {e}")
        return
    
    for row in all_rows:

        blocks_covered = [int(x.strip()) for x in row["Blocks Covered"].split(",")]

        dist_id = datetime.strptime(row["Timestamp"], "%m/%d/%Y %H:%M:%S").strftime("%y%m%d%H%M%S")

        for block in pg.blocks:
            
            if block.block in blocks_covered:
                
                existing_ids = [d for d in block.distributions]

                if dist_id not in block.deleted_distributions and dist_id not in existing_ids:
                    new_dist = Distribution(row["Name of organisation"], 
                                            row["Date of distribution"], 
                                            row["Type of Food distributed"], 
                                            row["Number of people catered to (estimate)"], 
                                            row["Were the food distributed halal certified?"])
                    block.log_distribution(dist_id, new_dist)
                    print(f"[DIAGNOSTIC] Prepared distribution '{dist_id}' for Block {block.block}")


    print(f"[SYNC LOG] Sync complete. Added new distribution(s).")

    return pg