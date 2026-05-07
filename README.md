_**cs32 final project**_
# _**Tracking Similar Language Use Across Competing News Publications**_

## **Description**
This tool allows a user to scrape posts from news publication's Telegram channels, determine which words were used most frequently across a date range, and identify common words shared between the channels. The tool scrapes data for presentation in datasets, frequency tables, and bar charts.

## **Instructions**
To use this tool you will need:
- Phone Number
- A Telegram Account
- Telegram API Key
- Telegram API Hash
- Links to the Telgram Channels you wish to compare

**Packages to install before use:**
- **Telethon** _Easily interfacing with Telegram's API_ `https://docs.telethon.dev/en/stable/`
- **Pandas** _Creating and manipulating dataframes_ `https://matplotlib.org/stable/index.html`
- **MatPlotLib** _Graphing Data Visualizations_ `https://pandas.pydata.org/docs/`
- **Stopword_List** _Cleaning Channel Messages_ `https://pypi.org/project/stop-words/`

**Python Library Packages that will be used:**
- **os** _easy directory pointing_
- **re** _regular expressions for message cleaning_
- **datetime** _datetime objects are used in message metadata_
- **sys** _error handling_
- **asyncio** _telethon requires asyncronous code running_

### **Steps to Run:**

**Signing up for Telegram and getting your api hash and key.**
1) If you do not have one already, create a Telegram account (you will need a phone number for this).
2) Log into your Telegram core to gain access to the Telegram API Development Tools.
3) Navigate to API Development Tools, press "Create new application", and input a short name and title for the project (e.g. "newscompare").
4) Save the resulting api_id and api_hash.

_(Ensure you have installed required packages before moving forward)_

**Running the Script**

_Quick Start_

1) Run `tool.py`.
2) Enter the API Key and API Hash.
3) Enter links to the Telgram channels you wish to compare (can be found by clicking on the channels profile page).
4) Enter the Start and End Dates of your desired comparison.

> **NOTE!** When you first run the script with an api key/hash pair, you will be creating a new session, which will require phone verification. The script will ask you to enter your phone number, then a code you recieve to the Telegram account your are signed in on. This only needs to be completed once. Be sure to include the country code when inputting your phone number.

> **NOTE!** As a default, the script will only pull the first 30 messages from a given range. To pull all messages from the range, set `message_limit` to `None`

_Preload Mode_

1) If you are running many comparisons in sequence and want to avoid re-entering your APU Key, Hash, desired channels, or date range, populate your preferences into lines 148-152 of `scraper.py`.
2) Set preload = True on line 10 of `scraper.py`.
3) Run `tool.py`

The script will output data, frequency tables, and visualizations in the same directory as the script. In the case there were no Telegram posts from a channel between the specified dates, the script will notify you, and prompt you to re-run the script.




