from functions import *
from art import *
from random import *

play_game = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if play_game == 'n' or play_game == 'no':
    clear()

elif play_game == 'y' or play_game == 'yes':
    print (logo)
    user_cards = []
    user_cards = deal_cards(deck, user_cards, 2)
    sumUser_cards = user_cards[0] + user_cards[1]
    print(f"    Your cards: {user_cards}, current score: {sumUser_cards}")
    compy_cards = []
    compy_cards = deal_cards(deck, compy_cards, 2)
    print(f"    Computer's first card: {compy_cards[0]}")

more_card = input("Type 'y' to get another card, type 'n' to pass: ")
while more_card == 'y':
    deal_cards(deck, user_cards, 1)
    # new_card = 6
    # user_cards.append(new_card)
    sumUser_cards = sumUser_cards + user_cards[-1]
    print(f"    Your cards: {user_cards}, current score: {sumUser_cards}")
    print(f"    Computer's first card: {compy_cards[0]}")
    more_card = input("Type 'y' to get another card, type 'n' to pass: ")
    # a = rand_pick(deck)
    # b = rand_pick(deck)

# a = rand_pick(deck)
# b = rand_pick(deck)
# print(a, b)