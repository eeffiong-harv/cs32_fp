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

    hash_valid = False
    while hash_valid == False :
        api_hash = input("What is your API Hash?")
        if len(api_hash) != 32 :
            print(f"'{api_hash}' invalid. (Ensure you input an 32 characters long)")
        else :
            hash_valid = True

    channel_loop = True
    channel_list = []
    link_valid = False

    while channel_loop == True :
        while link_valid == False:
            channel_input = input("What channel you would like to scrape?")
            if channel_input[0:12] != "https://t.me/" :
                link_valid = link_valid
            else:
                channel_list.append(channel_input)
                link_valid == True
        while len(channel_list) == 1:
            channel_input = input("What is the second channel you would like to scrape?")
            channel_list.append(channel_input)
        user_input_valid = False
        while user_input_valid == False :
            end_channel_loop = input("Would you like to add a channel? (y/n)")
            if end_channel_loop == "y" :
                channel_loop = channel_loop
                user_input_valid = True
            elif end_channel_loop == "n" :
                channel_loop = False
                user_input_valid = True
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
