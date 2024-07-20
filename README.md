# Flicks Scraper

This script scrapes www.flicks.com.au by given movie names from google sheet.

## Technologies Used
- Python
- GOOGLE SHEETs

## Installation

1. **Install Python**
   - You will need to have [Python](https://www.python.org/downloads/) installed.
   - When installing Python, ensure you check the `Add to PATH` checkbox.

2. **Install Required Packages**
   - Open your command prompt (cmd) and type the following commands to install the necessary packages:
     ```
     pip install requests
     pip install beautifulsoup4
     pip install lxml
     pip install gspread
     pip install pandas
     ```

3. **Download the Repository**
   - Download this repository's code from [GitHub](https://github.com/arnaldo31/flicks/archive/refs/heads/main.zip).

4. **Unzip the File**
   - Unzip the downloaded file. If you do not have an unzip application, you can download one [here](https://www.7-zip.org/a/7z2406-x64.exe).

## How to Use

1. Open the folder where this project is saved on your local machine.
2. Open this googl sheet to edit movie names that want to scrape [google sheets](https://docs.google.com/spreadsheets/d/1fMD-Ld9LOn8LctXuaFYywv3mY_LugjS1syd-bCizer0/edit?pli=1&gid=1789520897#gid=1789520897)
3. Go to google sheet tab `List of movies`
4. Run the `main.py` script:
5. Wait for the script to finish scraping.
6. Results will be save in the same google sheet 2nd tab name `Session times`

