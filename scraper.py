from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import datetime
import pandas

def main() :
    api_key = input("What is your API Key?")
        # Checks if the key is valid
    api_hash = input("What is your API Hash?")
        # Checks if the hash is valid
    channel_loop = True
    channel_list = []
    while channel_loop == True :

        channel_input = input("What channels would you like to scrape?")
        channel_list.append(channel_input)
        print(channel_list)
        print(len(channel_list))
        if len(channel_list) > 2 :
            valid_user_input = False
            while valid_user_input == False :
                end_channel_loop = input("Would you like to add a channel? (y/n)")
                if end_channel_loop == "y" :
                    channel_loop = channel_loop
                    valid_user_input = True
                elif end_channel_loop == "n" :
                    channel_loop = False
                    valid_user_input = True
                else:
                    print("Must select 'y' or 'n'. Try again...")

        # Loop of inputting channel name, checking for validity, and prompting for more
    client = TelegramClient(f'{channel_list} Scrape', api_key, api_hash)
    start_date = input("What is the start date of your scrape? (Format: YYYY-MM-DD)")
        # Checks if the date is valid
    end_date = input("What is the start date of your scrape? (Format: YYYY-MM-DD)")
        # Checks if the date is valid
    print(api_key, api_hash)

    print(f'Great! Attempting to join the {channel_list} TG channel(s) using Key: {api_key} and Hash: {api_hash}...')
        # Connect to telegram, report on success or failure
    # join()

    print(f'')
    return

def join(client) :
    return
main()
