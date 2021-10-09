from functions import *

play_game = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")

if play_game == 'n' or play_game == 'no':
    clear()
elif play_game == 'y' or play_game == 'yes':
    print("okay, cool! Let's play!")