from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import datetime
import pandas

def main() :
    api_key = input("What is your API Key?")
        # Checks if the key is valid
    api_hash = input("What is your API Hash?")
        # Checks if the hash is valid
    print(api_key, api_hash)
    return

main()
