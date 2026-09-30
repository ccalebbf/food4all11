import gspread
import streamlit as st
from datetime import datetime, date
from ZODB import DB
from ZODB.FileStorage import FileStorage
from persistent.list import PersistentList

import transaction

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

def data_to_db():

    pearl_garden = {98: 460098, 99: 460099, 
                100: 460100, 101: 460101, 
                102: 460102, 103: 460103, 
                104: 460104, 105: 460105, 
                106: 460106}

    # 1. Google Sheet Data to Python
    gc = get_gspread_client()
    spreadsheet = gc.open("Food Distribution Logging Form (Responses)").sheet1
    all_rows = spreadsheet.get_all_records(numericise_ignore=['all'])

    # 2. Creation of Database
    storage = FileStorage('Data.fs')
    db = DB(storage)
    connection = db.open()
    db_root = connection.root()
    
    # 3. Updating Data
    if 'neighbourhood' not in db_root:
        pg = Neighbourhood('Pearl Garden', [Block(key, pearl_garden[key]) for key in pearl_garden])
        db_root['neighbourhood'] = pg
        transaction.commit()
    else:
        n = db_root['neighbourhood']

    # 4. Populate Neighbourhood
    for row in all_rows:

        blocks_covered = [int(x.strip()) for x in row['Blocks Covered'].split(",")]

        dist_id = datetime.strptime(row['Timestamp'], "%m/%d/%Y %H:%M:%S").strftime("%y%m%d%H%M%S")

        for block in n.blocks:
            
            if block.block in blocks_covered:
                
                existing_ids = PersistentList(d for d in block.distributions)

                if dist_id not in block.deleted_distributions and dist_id not in existing_ids:
                    new_dist = Distribution(row['Name of organisation'], row['Date of distribution'], row['Type of Food distributed'], row['Number of people catered to (estimate)'], row['Were the food distributed halal certified?'])
                    block.log_distribution(dist_id, new_dist)

     # 5. Committing Changes
    transaction.commit()
    connection.close()
    db.close()
    print("Sync complete!")

if __name__ == "__main__":
    data_to_db()

