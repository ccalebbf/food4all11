# Food for All Database

Welcome! This is the GitHub repository responsible for running the codes behind the Food Distribution Database, a real-time tracker for food aid efforts conducted at the Pearl Garden neighbourhood in Bedok.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://foodforall11.streamlit.app/)

<div align="center">
<img src="images/bags.jpeg" alt="Descriptive Alt Text" width="50%">
</div>

## Key Features 🚀 
1. Log a distribution - via a Google Form on the home page
2. View summarised distribution records - via the map on the home page
3. View full records of individual blocks - via the block records page
4. Remove a distribution - via the block records page

## How it Works - a brief summary 📦
1. Food distribution records are recorded via a Google Form which is then transferred to a Google Sheet.
2. Python files (on this repository) reads the records from the Google Sheet and stores it into an object database.
3. Data from the object database is displayed on the website in the form of a map of the Pearl Garden neighbourhood, as well as tables of individual blocks and their records.

## Project Directory 📖
```text
food4all11/
├── .devcontainer/
│   ├── devcontainer.json
├── .streamlit/
│   ├── config.toml
├── images/
│   ├── bags.jpeg
│   ├── class_diagram.jpeg
│   ├── dist_bags.jpeg
├── pages/
│   ├── block_records.py
│   ├── home.py
├── .gitignore
├── README.md
├── app.py
├── google_sheets.py
├── map.py
├── models.py
├── requirements.txt
└── sync_updated.py
```

## Functions of each Files 📜
### models.py
Contains the Distribution, Block, and Neighbourhood classes, the building blocks of the database. The class hierarchy is as follows.
<div align="center">
<img src="images/class_diagram.png" alt="Descriptive Alt Text" width="30%">
</div>

### google_sheets.py
Contains all functions related to fetching/writing Google Sheet data.
| Function | Description |
| :--- | :--- |
| `get_gspread_client` | Establishes connection between Google Sheets and the Streamlit web app. |
| `fetch_sheet_records` | Fetches Google Sheet records in order to build the database. |
| `add_deletion_records` | Writes deleted distribution IDs (from the web app's Distribution Removal feature) into a separate sheet. |

### map.py
Contains functions related to constructing the interactive map of the Pearl Garden neighbourhood.
| Function | Description |
| :--- | :--- |
| `time_to_colour` | Maps the time since last distribution (of every block) to their representative colours.  |
| `create_pg_map` | Creates the map object. |

### sync_updated.py
Contains data_to_db, which processes the raw Google Sheet data into the object database. 

### app.py
Main page for Streamlit to run the app.

### home.py
Home page of the database, containing the following.
1. Introduction to the website
2. Shows summarised map of block records (last distribution, days since last distribution, total distributions)
3. Link to Google Form to log distributions

### block_records.py
Page for individual block records, containing the following.
1. Table of full distribution records for each block
2. Removal button for users to delete distributions

## Prerequisites
To adopt this project and run it on your own Streamlit app, you would have to have the following.
* A Google Account (for Google Sheets and Google Cloud Console)
* A GitHub Account
* A Streamlit Community Cloud Account (connected to the GitHub Account)

## Installation 🔧
To run this website on Streamlit, you would have to do the following.
### Step 1. Set up a Google Form
Do include the following MANDATORY fields in the exact phrasing. <br>
** Name of organisation** <br>
Short Answer Text <br>
**Date of distribution** <br>
Date <br>
**Neighbourhood** <br>
Multiple Choice (in this case, one neighbourhood, 'Pearl Garden') <br>
**Blocks Covered** <br>
Checkboxes (with the different blocks in the neighbourhood) <br>
**Type of Food distributed** <br> 
Short Answer Text <br>
**Number of people catered to (estimate)** <br>
Short Answer Text <br>
**Number of people catered to (estimate)** <br>
Short Answer Text <br>
**Were the food distributed halal certified?** <br>
Short Answer Text <br>


### Step 2: Set Up the Google Sheet
1. Make a Copy of the Template
* Open the [Template Google Sheet](https://docs.google.com/spreadsheets/d/1SuHBT_VcTySORDLElq1XTv3VRwXIOijrekMGioCqxzc/).
* Click **File** > **Make a copy** to save to your own Google Drive.
2. Note the Sheet URL
* Copy the new URL of your newly created Google Sheet (or the unique ID from the URL bar).
3. Link the Google Sheet to track responses of the Google Form created in Step 1.
### Step 3: Set Up Google Service Account Credentials
This is to allow the app to read and write data to your Google Sheet.
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (e.g. food-for-all)
3. Enable **Google Sheets API** and **Google Drive API**:
* Navigate to **APIs & Services** > **Library**.
* Search for both **Google Sheets API** and **Google Drive API** > click Enable.
4. Create a Service Account:
* Go to **APIs & Services** > **Credentials**.
* Click **Create Credentials** > **Service Account**.
* Name your service account, click **Create and Continue**, then **Done**.
5. Generate a Key:
* Click on the created service account and go to the **Keys** tab.
* Click **Add Key** > **Create New Key**.
* Select **JSON** and download the file. Keep this secure!
6. Share the Sheet with the Service Account:
* Open the JSON file downloaded and copy the ```client_email``` address.
* Go back to the Google Sheet and click **Share**.
* Paste the ```client_email``` address, give it editor permissions, and save.

### Step 4: Fork / Clone this Repository
Step 1: Fork the Repository
* Click the **Fork** button at the top-right of this GitHub repository to create a copy under your account.<br>
Step 2: Local Deployment (Optional)
```
# Clone your fork
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME

# Install dependencies
pip install -r requirements.txt
```
### Step 5: Deploy to Streamlit Community Cloud


### Step 6: Configure Streamlit Secrets
Be it deployment on Streamlit Cloud or running locally, you must provide your Google Service Account credentials and sheet details via Streamlit Secrets.

## Usage 🏡

## Authors 👥 
* Caleb F. ([@ccalebbf](https://github.com/ccalebbf))
### Special mention to my lovely teammates from NTU CNYSP!
* Chloe T.
* Darren T.
* Keira L.
* Sigmund K.
* Zeke N.
