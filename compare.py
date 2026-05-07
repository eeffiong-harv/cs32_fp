import pandas
import matplotlib.pyplot as plt

def compare_channels(channel_name_list, start_date, end_date) :
    print("\n--------------------[WORD COMPARISON PROCESS INTITIALIZED]--------------------")

    # Loading in Frequency Tables
    channel1 = pandas.read_csv(f"{channel_name_list[0]}_freq.csv", usecols = ['word', f'{channel_name_list[0]}_freq'])[0:21]
    channel2 = pandas.read_csv(f"{channel_name_list[1]}_freq.csv", usecols = ['word', f'{channel_name_list[1]}_freq'])[0:21]

    # Converting Frequency Tables to Lists
    channel1_list = pandas.Series.to_list(channel1['word'])
    channel2_list = pandas.Series.to_list(channel2['word'])

    # Creating new list of words that are present in both lists
    matchlist = []
    for channel1_word in range(len(channel1_list)) :
        for channel2_word in range(len(channel2_list)):
            if channel1_list[channel1_word] == channel2_list[channel2_word] :
                matchlist.append(channel1_list[channel1_word])

    # Displaying match count
    print(f'\n{channel_name_list[0]} and {channel_name_list[1]} have {len(matchlist)} frequently used words in common:\n')

    if len(matchlist) > 0 :

        # Merging datasets and only including shared words. This allows direct comparison of word frequency across channels.
        df_match = pandas.DataFrame(matchlist)
        df_match.columns = ['word']
        merged = df_match.merge(channel1, on = 'word').merge(channel2, on = 'word')

        # Displaying matched words and frequencies
        for matched_word in range(len(merged)) :
            print(f'> The word "{merged["word"][matched_word]}" was used {merged[f'{channel_name_list[0]}_freq'][matched_word]} times by {channel_name_list[0]} and {merged[f'{channel_name_list[1]}_freq'][matched_word]} times by {channel_name_list[1]}.')

        # Producing Comparison Graph
        merged.plot.bar(x = 'word', y = [f'{channel_name_list[0]}_freq', f'{channel_name_list[1]}_freq'])
        plt.xlabel("Term")
        plt.ylabel("Number of Occurances")
        plt.title(f"Shared Words in Top-20 list by Frequency for {channel_name_list[0]} and {channel_name_list[1]} between {start_date.strftime('%b %d, %Y')} and {end_date.strftime('%b %d, %Y')}")
        plt.savefig(f'comparison_graph.png', bbox_inches = 'tight')

    # Case when there are no frequent word matches
    else:
        print("Without frequently used words in common, there is no Comparison Graph to produce.")

    print("\n--------------------[WORD COMPARISON PROCESS COMPLETE]--------------------")
    print(f"\nPublication Scraping and Comparision Complete!\n\n> Raw Message Data (and Metadata) saved as '{channel_name_list[0]}_messages.csv' and '{channel_name_list[1]}_messages.csv'.\n> Frequency Tables saved as '{channel_name_list[0]}_freq.csv' and '{channel_name_list[0]}_messages.csv'.\n> Visualizations/Charts are saved as '{channel_name_list[0]}_graph.csv', '{channel_name_list[0]}_graph.csv', and 'comparison_graph.csv' (if applicable).\n\nAll Data and Visualizations saved to the same directory you ran this script in!")
