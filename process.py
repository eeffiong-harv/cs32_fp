import pandas
import re
from stop_words import get_stop_words # list of stopwords for cleaning messages
import matplotlib.pyplot as plt # data visualization


def process_channel(channel, name, start_date, end_date) :
    print("\n--------------------[FREQUENT WORD IDENTIFICATION PROCESS INITIALIZED]--------------------")
    print(f'\nIdentifying Most Frequently Terms in {name} Posts...')

    # Loading in Stopwords and Channel messages. Creating empty list to populate with words from messages.
    stop_word_list = get_stop_words("en")
    channel_messages = pandas.Series.tolist(channel["Message"])
    messagelist = []

    # Cleaning the messages
    for i in range(len(channel_messages)) :
        message = channel_messages[i].lower().strip() # lowercase
        message = message.replace('\n', ' ') # removing line breaks
        message = re.sub(r'https?://\S+', '', message) # removing urls

        # Removing punctuation and special characters
        newmessage = ""
        for char in message :
            if char.isalpha() == True or char.isdigit == True or char == ' ' or char == '-':
                newmessage += char

        # Converting messages into single list of words
        newmessage = newmessage.split(" ")
        for item in newmessage :
            if item != '' and item != ' ' and item != '-' :
                if item not in stop_word_list:
                    messagelist.append(item)

    # Creating a frequency table from the list of words and saving as csv
    frequency_table = pandas.Series(messagelist)
    frequency_table = frequency_table.value_counts().reset_index()
    frequency_table.columns = ['word', f'{name}_freq']
    frequency_table.to_csv(f"{name}_freq.csv")

    # Displaying Frequency Table for top 20 words
    print(f'\nTop 20 Most Frequently Used Words in {name} Posts:\n{frequency_table[1:21]}')

    # Producing Bar Graph of Frequency Table for top 20 words
    frequency_table[1:21].plot.bar(x = 'word', y = f'{name}_freq')
    plt.xlabel("Term")
    plt.ylabel("Number of Occurances")
    plt.title(f"20 Most Frequently used Words in {name} posts between {start_date.strftime('%b %d, %Y')} and {end_date.strftime('%b %d, %Y')}")
    plt.savefig(f'{name}_graph.png', bbox_inches = 'tight')
    print("\n--------------------[FREQUENT WORD IDENTIFICATION PROCESS COMPLETE]--------------------")
    return

