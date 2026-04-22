from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import datetime
import pandas
import re

def main() :

    # key_valid = False
    # while key_valid == False :
    #     api_key = input("What is your API Key?")
    #     if api_key.isdigit() != True or len(api_key) != 8 :
    #         print(f"'{api_key}' invalid. (Ensure you input an 8 digit key)")
    #     else :
    #         key_valid = True

    # hash_valid = False
    # while hash_valid == False :
    #     api_hash = input("What is your API Hash?")
    #     if len(api_hash) != 32 :
    #         print(f"'{api_hash}' invalid. (Ensure you input an 32 characters long)")
    #     else :
    #         hash_valid = True

    # channel_loop = True
    # channel_list = []
    # link_valid = False

    # while channel_loop == True :
    #     while link_valid == False:
    #         channel_input = input("What channel you would like to scrape?")

    #         if channel_input[0:13] != "https://t.me/" :
    #             print(f"'{channel_input}' is an invalid link. Try again... (ensure link begins with 'https://t.me/')")
    #             link_valid = link_valid
    #         else:
    #             channel_list.append(channel_input)
    #             link_valid == True
    #             print(channel_list, "SUCCESS")
    #             break

    #     while len(channel_list) == 1:
    #         channel_input = input("What is the second channel you would like to scrape?")
    #         channel_list.append(channel_input)
    #     user_input_valid = False
    #     while user_input_valid == False :
    #         end_channel_loop = input("Would you like to add a channel? (y/n)")
    #         if end_channel_loop == "y" :
    #             channel_loop = channel_loop
    #             user_input_valid = True
    #         elif end_channel_loop == "n" :
    #             channel_loop = False
    #             user_input_valid = True
    #         else:
    #             print("Must select 'y' or 'n'. Try again...")

    #     # Loop of inputting channel name, checking for validity, and prompting for more
    # # client = TelegramClient(f'{channel_list} Scrape', api_key, api_hash) # NEED TO FIX FIRST VALUE
    # current_channel_num = 0
    # current_channel = channel_list[current_channel_num]
    # print(current_channel)
    start_date_valid = False
    while start_date_valid == False :
        start_date = input("What is the start date of your scrape? (Format: YYYY-MM-DD)")
        try :
            if re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", start_date).span() != (0, 10) :
                print(f"'{start_date}' is an invalid input. Try again...")
            else:
                start_date = datetime.datetime(int(start_date[0:4]), int(start_date[5:7]), int(start_date[8:10]), tzinfo=datetime.timezone.utc)
                start_date_valid = True
        except :
            AttributeError
            print(f"'{start_date}' is an invalid input. Try again...")

    end_date_valid = False
    while end_date_valid == False :
        end_date = input("What is the end date of your scrape? (Format: YYYY-MM-DD)")
        try :
            if re.fullmatch(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])", end_date).span() != (0, 10) :
                print(f"'{end_date}' is an invalid input. Try again...")
            else:
                end_date = datetime.datetime(int(end_date[0:4]), int(end_date[5:7]), int(end_date[8:10]), tzinfo=datetime.timezone.utc)

                if start_date > end_date :
                    print(f"'{end_date}' comes before the start date. Try again...")
                else :
                    end_date_valid = True
        except :
            AttributeError
            print(f"'{end_date}' is an invalid input. Try again...")


    print(api_key, api_hash)

    print(f'Great! Attempting to join the {channel_list} TG channel(s) using Key: {api_key} and Hash: {api_hash}...')
        # Connect to telegram, report on success or failure
    # join()

    print(f'')
    return

def join(client) :
    return
main()
