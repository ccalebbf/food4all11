import gspread
from ZODB import DB
from ZODB.FileStorage import FileStorage
import transaction

from models import Distribution, Block, Neighbourhood

pearl_garden = {98: 460098, 99: 460099, 
                100: 460100, 101: 460101, 
                102: 460102, 103: 460103, 
                104: 460104, 105: 460105, 
                106: 460106}

pg = Neighbourhood('Pearl Garden', [Block(key, pearl_garden[key]) for key in pearl_garden])

def data_to_db():

    # 1. Google Sheet Data to Python
    gc = gspread.service_account(filename = 'food_for_all.json')
    spreadsheet = gc.open("Food Distribution Logging Form (Responses)").sheet1
    all_rows = spreadsheet.get_all_records()

    # 2. Creation of Database
    storage = FileStorage('Data.fs')
    db = DB(storage)
    connection = db.open()
    db_root = connection.root()

    # 3. Populate Neighbourhood
    for row in all_rows:
    
        if isinstance(row['Blocks Covered'], int):
            row['Blocks Covered'] = str(row['Blocks Covered'])

        blocks_covered = [int(x.strip()) for x in row['Blocks Covered'].split(",")]
        
        for block in pg.blocks:
            if block.block in blocks_covered:
                new_dist = Distribution(row['Name of organisation'], row['Date of distribution'], row['Type of Food distributed'], row['Number of people catered to (estimate)'])
                block.log_distribution(new_dist)

    # 4. Updating Data.fs
    db_root['neighbourhood'] = pg

    # 5. Committing Changes
    transaction.commit()
    connection.close()
    db.close()
    print("Sync complete!")

if __name__ == "__main__":
    data_to_db()