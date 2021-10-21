from functions import *
from art import *
from random import *

play_game = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#dealing the initial cards
if play_game == 'y' or play_game == 'yes':
    clear()
    print (logo)
    user_cards = []
    user_cards = deal_cards(deck, user_cards, 2)
    sumUser_cards = user_cards[0] + user_cards[1]
    print(f"    Your cards: {user_cards}, current score: {sumUser_cards}")
    compy_cards = []
    compy_cards = deal_cards(deck, compy_cards, 2)
    print(f"    Computer's first card: {compy_cards[0]}")

    #cont dealing cards
    more_card = input("Type 'y' to get another card, type 'n' to pass: ")

    sumCompy_cards = card_add(compy_cards)
    if more_card == 'n' or sumUser_cards >= 21:
        determine_winner(sumUser_cards, sumCompy_cards)

    print(' ')
    while more_card == 'y':
        if sumUser_cards <= 21:
            deal_cards(deck, user_cards, 1)
            sumUser_cards = sumUser_cards + user_cards[-1]
            compy_cards = cardAdd4Compy(compy_cards, deck)
            print(f"    Your cards: {user_cards}, current score: {sumUser_cards}")
            print(f"    Computer's first card: {compy_cards[0]}")
            if sumUser_cards <= 21:
                more_card = input("Type 'y' to get another card, type 'n' to pass: ")
            else:
                more_card = 'n'
            

    sumCompy_cards = card_add(compy_cards)
    if more_card == 'n':
        win = determine_winner(sumUser_cards, sumCompy_cards)
        print(' ')
        if win == 'Y':
            print(f"Your final score: {sumUser_cards} \n The Computer's score: {sumCompy_cards} \n You Won!!")
        elif win == 'N':
            print(f"Your final score: {sumUser_cards} \n The Computer's score: {sumCompy_cards} \n You Lost!!")
        elif win == 'D':
            print(f"Your final score: {sumUser_cards} \n The Computer's score: {sumCompy_cards} \n It's a Draw!!")

if play_game == 'n' or play_game == 'no':
    clear()