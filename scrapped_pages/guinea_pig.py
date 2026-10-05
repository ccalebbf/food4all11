# Helper to retrieve Distribution Data
@st.cache_data(ttl=30, show_spinner = False)
def fetch_distribution_records(_gc):
    spreadsheet = _gc.open("Food Distribution Logging Form (Responses)")
    distributions_records = spreadsheet.worksheet("Form Responses 2") 
    return distributions_records.get_all_records(numericise_ignore=['all'])

# Helper to retrieve deleted Distribution IDs (Failsafe for site reboots)
    # block - block to obtain deleted records for
    # del_dists - each block's unique PersistentList of deleted IDs
@st.cache_data(ttl=30, show_spinner = False)
def fetch_deletion_records(_gc, block):
    spreadsheet = _gc.open("Food Distribution Logging Form (Responses)")
    deletion_records = spreadsheet.worksheet("DeletedIDs") 

    header_cell = deletion_records.find(str(block), in_row = 1)

    if header_cell:
        
        col_values = deletion_records.col_values(header_cell.col)

        return [val for val in col_values[1:] if val.strip()]

    return []