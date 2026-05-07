import os # easy directory pointing
import asyncio # asynchronous processes for telethon
import pandas # working with databases
from compare import compare_channels
from process import process_channel
from scraper import main

directory = os.path.dirname(os.path.abspath(__file__))

# Telgram Scraping Process
scrape_results = asyncio.run(main())
channel_name_list = scrape_results[0]
start_date = scrape_results[1]
end_date = scrape_results[2]

# Cleaning message data and producing frequency tables + graphs for each channel
for name in channel_name_list :
    channel = pandas.read_csv(f"{directory}/{name}_messages.csv")
    process_channel(channel, name, start_date, end_date)

# Identifying shared frequent words and producing comparison graphs
compare_channels(channel_name_list, start_date, end_date)


