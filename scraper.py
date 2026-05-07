from telethon import TelegramClient # Connecting to & Interacting with Telgram API
from telethon.tl.functions.channels import JoinChannelRequest
import datetime # For using date objects (how info is stored in telegram)
import pandas # For creating and exporting dataframes
import re # For using regex (validating user entries)
import sys
import asyncio # For running asynchronous code (Telethon library employs this)


preload = True # Set to 'True' to run with preloaded user information and channel list
messagelimit = None # Set to an integer or None

# Function to Join Telegram Channel
async def join(client, current_channel) :

    try:
        await client.start() #logging in and connecting to telegram client
        print(f"\nAttempting to join {current_channel}...")
        await client(JoinChannelRequest(current_channel)) # joining specified channel
        print(f"Successfully joined {current_channel}!\n")

    except:
        print(f"Failed to join {current_channel}.")
        return

# Function for Scraping telegram channels and saving as .csv
posts_found = True
async def scrape(client, current_channel, start_date, end_date, limit = messagelimit) :
    print(f"Attempting to scrape {current_channel[13:]} posts from {start_date.strftime('%b %d, %Y')}-{end_date.strftime('%b %d, %Y')}...")

    message_data = [] # list to collect messages + metadata
    message_df = pandas.DataFrame(message_data, columns = ['ID', 'Date', 'Message', 'Views', 'Channel']) # df w/ columns for messages + metadata

    # Adding messages containing text to the list
    async for message in client.iter_messages(current_channel, limit, offset_date = start_date, reverse = True) :
        if message.text:
            message_data.append([message.id, message.date, message.text, message.views, f"{current_channel[13:]}"])
        if message.date > end_date :
            break
    # Creating and exporting .csv of messages + metadata

    if message_data :
        message_df = pandas.DataFrame(message_data, columns = ['ID', 'Date', 'Message', 'Views', 'Channel'])
        message_df.to_csv(f'{current_channel[13:]}_messages.csv', encoding = 'utf-8')
        print(f"Finished scraping {current_channel}. {len(message_data)} Messages saved to {current_channel[13:]}_messages.csv.")
        posts_found = True
    else :
        print(f"No {current_channel[13:]} posts found during specified period.")
        posts_found = False


    return message_df, posts_found

# Function for retrieving user info
async def setup() :

    # Retrieving user API Key
    key_valid = False
    while key_valid == False :
        api_key = input("\nWhat is your API Key? ")
        if api_key.isdigit() != True or len(api_key) != 8 :
            print(f"'{api_key}' invalid. (Ensure you input an 8 digit key)")
        else :
            key_valid = True
    # Retrieving user API Hash
    hash_valid = False
    while hash_valid == False :
        api_hash = input("What is your API Hash? ")
        if len(api_hash) != 32 :
            print(f"'{api_hash}' invalid. (Ensure you input an 32 characters long)")
        else :
            hash_valid = True

    # Retrieving channel list
    channel_loop = True
    channel_list = []
    link_valid = False

    while channel_loop == True :

        # First and Third+ Channels
        while link_valid == False:
            channel_input = input("\nWhat channel you would like to scrape? ")

            if channel_input[0:13] != "https://t.me/" :
                print(f"'{channel_input}' is an invalid link. Try again... (ensure link begins with 'https://t.me/')")
                link_valid = link_valid
            else:
                channel_list.append(channel_input)
                link_valid = True
                print(f"\n{channel_input[13:]} added to channel list.")
                break

        # Second Channel
        while len(channel_list) == 1:
            channel_input = input(f"\nWhat is the second channel you would like to scrape? ")
            if channel_input[0:13] != "https://t.me/" :
                print(f"'\n{channel_input}' is an invalid link. Try again... (ensure link begins with 'https://t.me/')")
                link_valid = link_valid
            else:
                channel_list.append(channel_input)
                link_valid = True
                print(f"\n{channel_input[13:]} added to channel list.")
                break

        channel_loop = False ## <-- Limits Comparison to 2 Channels
        user_input_valid = True ## <-- Limits Comparison to 2 Channels

    # Retrieving start date
    start_date_valid = False
    while start_date_valid == False :
        start_date = input("\nWhat is the start date of your scrape? (Format: YYYY-MM-DD) ")
        try :
            if re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", start_date).span() != (0, 10) :
                print(f"'{start_date}' is an invalid input. Try again...")
            else:
                start_date = datetime.datetime(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]), tzinfo=datetime.timezone.utc)
                start_date_valid = True
        except :
            print(f"'{start_date}' is an invalid input. Try again...")

    # Retrieving end date
    end_date_valid = False
    while end_date_valid == False :
        end_date = input("What is the end date of your scrape? (Format: YYYY-MM-DD) ")
        try :
            if re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", end_date).span() != (0, 10) :
                print(f"'{end_date}' is an invalid input. Try again...")
            else:
                end_date = datetime.datetime(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]), tzinfo=datetime.timezone.utc)

                if start_date > end_date :
                    print(f"'{end_date[0:10]}' comes before the start date. Try again...")
                else :
                    end_date_valid = True
        except :
            print(f"'{end_date}' is an invalid input. Try again...")

    print(f"Great! Let's start scraping {len(channel_list)} channels")
    return api_key, api_hash, channel_list, start_date, end_date


# Main Function
async def main() :
    # Enter user info + parameters here to skip q&a phase
    if preload == True:
        print("Welcome to NewScraper: a tool designed to scrape and compare word usage from the Telegram posts of News Publications.\nRunning with preloaded user info & channel list...")
        api_key = '14913236'
        api_hash = 'b1bdcf76b1a430359e766da11638714e'
        channel_list = ['https://t.me/nytimes','https://t.me/BBCWorld']
        start_date = datetime.datetime(2024, 1, 1, tzinfo=datetime.timezone.utc)
        end_date = datetime.datetime(2024, 1, 31, tzinfo=datetime.timezone.utc)
    else:
        print("Welcome to NewScraper: a tool designed to scrape and compare word usage from the Telegram posts of News Publications.")
        api_key, api_hash, channel_list, start_date, end_date = await setup() # Run setup() function to collect info + parameters
    print("\n--------------------[SCRAPING PROCESS INITIALIZED]--------------------")
    client = TelegramClient('session_name', api_key, api_hash) # Building client (Each time session name is updated, phone number will need to be re-entered/verified).

    current_channel_num = 0
    for channel in channel_list : # Looping through each channel in the list
        current_channel = channel_list[current_channel_num]
        await join(client, current_channel) # Joining telegram channel
        posts_found = await scrape(client, current_channel, start_date, end_date) # Scraping messages according to parameters
        if posts_found[1] == False : # Case when there are no posts in a specified date range.
            sys.exit("\nERROR: One or more channels has no posts between the specified dates. Please retry the script with new dates.")
        current_channel_num += 1
    print(f"\nCompleted scraping messages from all channels!")
    print("\n--------------------[SCRAPING PROCESS COMPLETE]--------------------")
    channel_name_list = []
    for a in channel_list :
        channel_name_list.append(a[13:])
    return channel_name_list, start_date, end_date

if __name__ == "__main__":
    asyncio.run(main())
