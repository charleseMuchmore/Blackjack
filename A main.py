from functions import *
from art import *
from random import *

play_game = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
if play_game == 'n' or play_game == 'no':
    clear()
#dealing the initial cards
elif play_game == 'y' or play_game == 'yes':
    print (logo)
    user_cards = []
    user_cards = deal_cards(deck, user_cards, 2)
    sumUser_cards = user_cards[0] + user_cards[1]
    print(f"    Your cards: {user_cards}, current score: {sumUser_cards}")
    compy_cards = []
    compy_cards = deal_cards(deck, compy_cards, 2)
    # print(f"    Computer's first card: {compy_cards[0]}")
    print(f"    Computer's cards: {compy_cards}")

#cont dealing user cards
more_card = input("Type 'y' to get another card, type 'n' to pass: ")
while more_card == 'y':
    deal_cards(deck, user_cards, 1)
    sumUser_cards = sumUser_cards + user_cards[-1]
    #cont dealing compy cards
    compy_cards = cardAdd4Compy(compy_cards, deck)
    print(f"    Your cards: {user_cards}, current score: {sumUser_cards}")
    # print(f"    Computer's first card: {compy_cards[0]}")
    print(f"    Computer's cards: {compy_cards}")
    more_card = input("Type 'y' to get another card, type 'n' to pass: ")

#cont dealing compy cards
    
# if more_card == 'n':
