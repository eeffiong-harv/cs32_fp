### 04/22/26

Libraries used
---
Telethon : telegram api to grab information from telgram through individual api
Pandas : Saving and organizing information into a csv



- prompt user to enter (and save) api key and hash
- prompt user to enter telegram channels
- prompt user for confirmation
- scraping loop
    - grab id, datetime, message, views
    - save to master csv

### 04/24/26

Structure of the scraping script
- Query user for api key, api hash, channels, and start and end dates.
- Connect to client
- For each channel in the list:
    - Connect to channel
    - Add messages + metadata to list
    - convert list to dataframe
    - export dataframe

Using libraries: re, asyncio, datetime
