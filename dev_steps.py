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
            ###Not sure how to put it next to the cards###

        ##display compy's first card --> randomly choose two cards from a deck of cards
            ###do the same thing you did for choosing for the user
        ##display compy's first card --> display only one to the user
            ###fetch only the first index in the list, putting it in a variable
            ###display that variable as the compy's card

        ##display option to get another card or no --> display an option to get another card or no
            #get_card = input("Would you like to take another card? Type 'y' to take another card, 'n' to pass: ")
       