from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import datetime
import pandas

def main() :
    key_valid = False
    while key_valid == False :
        api_key = input("What is your API Key?")
        if api_key.isdigit() != True or len(api_key) != 8 :
            print(f"'{api_key}' invalid. (Ensure you input an 8 digit key)")
        else :
            key_valid = True

    api_hash = input("What is your API Hash?")
        # Checks if the hash is valid
    channel_loop = True
    channel_list = []
    while channel_loop == True :

        channel_input = input("What channel you would like to scrape?")
        channel_list.append(channel_input)
        while len(channel_list) == 1:
            channel_input = input("What is the second channel you would like to scrape?")
            channel_list.append(channel_input)
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
