from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
import datetime
import asyncio
import pandas
import re




async def join(client, current_channel) :
    try:
        print("Connecting to client...")
        await client.start() #logging in and connecting to telegram client
        print("Connection successful!")
        print(f"Attempting to join {current_channel}...")
        await client(JoinChannelRequest(current_channel)) # joining specified channel
        print(f"Successfully joined {current_channel}!")
    except:
        print(f"Failed to join {current_channel}.")
        return

async def scrape(client, current_channel, limit = 20) :
    message_data = []
    async for message in client.iter_messages(current_channel, limit, offset_date = start_date, reverse = True) :
        if message.text:
            # print(message.text)
            message_data.append([message.id, message.date, message.text, message.views, f"{current_channel[13:]}"])
        message_df = pandas.DataFrame(message_data, columns = ['ID', 'Date', 'Message', 'Views', 'Channel'])
        message_df.to_csv(f'{current_channel[13:]}_messages.csv', encoding = 'utf-8')
        if message.date > end_date :
            break
    return message_df

async def setup() :

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

            if channel_input[0:13] != "https://t.me/" :
                print(f"'{channel_input}' is an invalid link. Try again... (ensure link begins with 'https://t.me/')")
                link_valid = link_valid
            else:
                channel_list.append(channel_input)
                link_valid = True
                print(channel_list, "SUCCESS")
                break

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
                    print(f"'{end_date[0:10]}' comes before the start date. Try again...")
                else :
                    end_date_valid = True
        except :
            AttributeError
            print(f"'{end_date}' is an invalid input. Try again...")

    print(f"Great! Let's start scraping {len(channel_list)} channels")
    return api_key, api_hash, channel_list, start_date, end_date

async def main() :
    auto = True
    if auto == True:
        api_key = '14913236'
        api_hash = 'b1bdcf76b1a430359e766da11638714e'
        current_channel = 'https://t.me/nytimes'
        start_date = datetime.datetime(2026, 2, 1, tzinfo=datetime.timezone.utc)
        end_date = datetime.datetime(2026, 4, 1, tzinfo=datetime.timezone.utc)
    else:
        await setup()

    # current_channel_num = 0
    # current_channel = channel_list[current_channel_num]
    client = TelegramClient('session_name', api_key, api_hash) # Each time session name is updated, phone number will need to be re-entered.

    connection =  await join(client, current_channel)
    print(connection)

    scraper = await scrape(client, current_channel)
    print(scraper)
    print(f"Finished scraping {current_channel}. Messages saved to {current_channel[13:]}_messages.csv.")
    # print(f"Attempting to scrape {current_channel[13:]} posts from between {start_date.strftime('%b %d, %Y')} and {end_date.strftime('%b %d, %Y')}")

    return

if __name__ == "__main__":
    asyncio.run(main())
