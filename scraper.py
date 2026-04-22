from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import datetime
import pandas

def main() :
    api_key = input("What is your API Key?")
        # Checks if the key is valid
    api_hash = input("What is your API Hash?")
        # Checks if the hash is valid
    channels = input("What channels would you like to scrape?")
        # Loop of inputting channel name, checking for validity, and prompting for more
    print(api_key, api_hash)

    print(f'Great! Attempting')
    return

main()
