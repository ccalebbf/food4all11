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
│   ├── log_distribution.png
│   ├── remove_distribution.png
│   ├── reset_deletions.png
│   ├── reset_distributions.png
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

## About the Files 📜
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
| Field | Type |
| :--- | :--- |
| Name of organisation | Short Answer Text |
| Date of distribution | Date |
| Neighbourhood | Multiple Choice (One neighbourhood, 'Pearl Garden' in this case) |
| Blocks Covered | Checkboxes (with the different blocks in the neighbourhood) |
| Type of Food distributed | Short Answer Text |
| Number of people catered to (estimate) | Short Answer Text |
| Were the food distributed halal certified? | Short Answer Text |

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
1. Fork the Repository:
* Click the **Fork** button at the top-right of this GitHub repository to create a copy under your account. 
2. Local Deployment (Optional)
```
# Clone your fork
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME

# Install dependencies
pip install -r requirements.txt
```

### Step 5: Configure Streamlit Secrets
Be it deployment on Streamlit Cloud or running locally, you must provide your Google Service Account credentials and sheet details via Streamlit Secrets. The required format (```secrets.toml```) is as such.
```
# URL or ID of your Google Sheet
spreadsheet = "https://docs.google.com/spreadsheets/d/YOUR_SPREADSHEET_ID/edit"

[gcp_service_account]
type = "service_account"
project_id = "YOUR_PROJECT_ID"
private_key_id = "YOUR_PRIVATE_KEY_ID"
private_key = "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n"
client_email = "YOUR_SERVICE_ACCOUNT_EMAIL@YOUR_PROJECT.iam.gserviceaccount.com"
client_id = "YOUR_CLIENT_ID"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/YOUR_SERVICE_ACCOUNT_EMAIL"
```
Note: Copy the field values directly from the JSON file downloaded in Step 3. Keep the quotes around strings, and preserve line breaks (\n) in ```private_key```.
### Step 6: Deploy to Streamlit Community Cloud
1. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
2. Click **New app**.
3. Select your GitHub repository, branch (e.g. ```main```), and main file path (e.g. ```app.py```).
4. Click **Advanced settings...** before deploying.
5. Paste formatted secrets (from Step 5) into the **Secrets** text field.
6. Click Deploy!

## Usage 🏡

### Logging a distribution
This is done through the Google Form on the Home Page! The Google Form link is attached under the header that says "Log Distribution Here".

<div align="center">
<img src="images/log_distribution.png" alt="Descriptive Alt Text" width="75%">
</div>

### Removing a distribution
This is done through the "Remove a Distribution" feature on the Block Records Page! Navigate to the desired block, and enter the Distribution ID of the Distribution you wish to remove.

<div align="center">
<img src="images/remove_distribution.png" alt="Descriptive Alt Text" width="75%">
</div>

### Resetting all distributions (done by app host only)
This is done through the Google Form.

**Distribution Records**

Delete all rows **below the header row** on the sheet that tracks Google Form responses.

<div align="center">
<img src="images/reset_distributions.png" alt="Descriptive Alt Text" width="75%">
</div>

**Deletion Records**

Delete all entries **below the header row** on the sheet that stores deleted Distribution IDs.

<div align="center">
<img src="images/reset_deletions.png" alt="Descriptive Alt Text" width="75%">
</div>

## Authors 👥 
* Caleb F. ([@ccalebbf](https://github.com/ccalebbf))
### Special Mentions
Huge thanks to my lovely teammates from NTU CNYSP (NH0001 Team 11) for their support!
* Chloe T.
* Darren T.
* Keira L.
* Sigmund K.
* Zeke N.
