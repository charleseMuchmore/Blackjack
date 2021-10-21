#play_game = input("Do you want to play a game of Blackjack? type 'y' or 'n': ")
    #n --> close program

    #y --> display art, your cards, current score, compy's first card, and then if they want to get another card or no
        ##display art --> import from art file and print 
            
        ##display cards --> randomly choose two cards from a deck of cards
            ###create a list with all the numbers of a deck of cards
            ###use the random method to randomly select 2 numbers from that list
            ###put those numbers in their own list
        ##display cards --> Display the numbers to the user like so "[7, 5]"
            ###print the list with the two numbers in it
            
        ##display current score --> add up the sum of the user's two cards
            ###fetch the two numbers from the user's hand
            ###add them, and place in a variable
        ##display current score --> display (next to their cards)
            ###print the variable with the score 
            ###Put next to user's cards###

        ##display compy's first card --> randomly choose two cards from a deck of cards
            ###do the same thing you did for choosing for the user
        ##display compy's first card --> display only one to the user
            ###fetch only the first index in the list, putting it in a variable
            ###display that variable as the compy's card

        ##display option to get another card or no --> display an option to get another card or no
            ###get_card = input("Would you like to take another card? Type 'y' to take another card, 'n' to pass: ")

#more_card = input("Type 'y' to get another card, type 'n' to pass: ")

    #The compy needs to get it's cards too. It should be able to do more than 2
    #y -->

    #n --> display user's hand and score, and compy's hand and final score. Determine who won, or if its a draw. prompt to play again. 
        ##display user's hand --> Print out the user's hand and score as their final hand and final score

        ##display compy's hand --> Print out the compy's final hand and score
#GENERAL RULES#
# The deck is unlimited in size.
# There are no jokers.
# The Jack/King/Queen all count as 10.
# The Ace can count as 11 or 1.
# Uses the following list for a deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn. 



##TO Upgrade##
#Make the deck more realistic
#add Jokers??
#Make the compy card picking algorythm account for chance
#possibly add more Ai, and maybe even capability for more players?
#add user friendly error messages for invalid inputs
#perhaps make different difficulty levels
#maybe add a functionalty to keep track of score over multiple rounds