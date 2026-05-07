# CODE GRAVEYARD
### Code Allowing for Additional Channels to be added to comparison. Did not fully build out this feature.
*After Second Channel input:*

    # Optional >2 Channels
    while user_input_valid == False :
        end_channel_loop = input(f"\nCurrent Channel List:\n{channel_list}\n\nWould you like to add a channel? (y/n) ")
        if end_channel_loop == "y" :
            channel_loop = channel_loop
            user_input_valid = True
            link_valid = False
        elif end_channel_loop == "n" :
            channel_loop = False
            user_input_valid = True
        else:
            print("Must select 'y' or 'n'. Try again...")

Next steps:
Better interpretation - proportion of posts using the word may be a better indicator than raw count
Need to build out >2 channels
Better way of saving channel list, api keys, etc for easy search
Better folder export organization
