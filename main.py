# BlackJack Game! 
# First, import logo from art.py
from art import logo 

# Next import the rest of the modules that will be used in this project
import os
import random 

# There is not a command in VS code to clear the console when we want, so this "os" is a workaround 
# using the OS module, we can create the following function: 

def clear():
    """Clears the console""" #Note this is the proper use of a Docstring - to inform the programmer looking at the code about something happening. Documentation. 
    command = 'clear'
    # If statement to check to see what OS computer is running. The "clear" command in Windows is "cls" so if the computer is running windows it changes the command so it works as desired
    if os.name in ('nt', 'dos'):
        command = 'cls'
        # inputs the command variable into the system function from the os module, this executes the command in the console/terminal 
    os.system(command)

# Function to 'pull' a card or deal from the deck at random. 
def deal_card():
    # Create Docstring to indicate what this does 
    """Returns a random card from the deck"""
    # Create a cards list for each card, Ace (11) through King (10)
    # Note Royalty/face cards are all 10, Ace is 11. Rules state it can also be 1; we'll deal with that later. 
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
    # Use random module to generate a random card value from the cards list. The choice method passes in the cards list and sets the output to a variable 
    card = random.choice(cards)
    # Use the Return keyword to return a result - the card variable 
    return card 

# Function to keep score of current cards pulled from the deck 
def calculate_score(cards): #note - this 'cards' argument is separate from the cards variable in the above function because of scope. 
    """Takes a list of cards and returns the total score calculated. Keeps score as user plays the game"""
    # Create an If statement to check if a player has a Black Jack Hand (2 card 21)
    if sum(cards) == 21 and len(cards) == 2: #sum() and len() are both built-in functions 
        #return 0 to represent our BlackJack hand, we will use this instead of 21 to differentiate the normal score of 21 
        return 0
    # Create an if statement that says if 11 is in the cards, and the sum is less than 21, change 11 to 1 so as to not bust 
    if 11 in cards and sum(cards) > 21: 
        cards.remove(11)
        cards.append(1)
    # Return the sum of the cards after all the above if statements have been checked 
    return sum(cards)

# Create a function that compares the scores and returns an outcome 
def compare(user_score, computer_score): #pass in user's score and computer's score as arguments 
    """Pass in user & computer scores as arguments"""
    # Use if/elif/else statements for each outcome 
    # Draw
    if user_score == computer_score:
        return "Draw"
    # Computer has BlackJack 
    elif computer_score == 0:
        return "Opponent has BlackJack. You lost this round."
    # User has BlackJack 
    elif user_score == 0: 
        return "You win with a BlackJack! Congrats!"
    # User busts (goes over 21)
    elif user_score > 21: 
        return "You busted - score is over 21. Better luck next time!"
    # Computer busts 
    elif computer_score > 21: 
        return "Opponent went over. You win!"
    # User wins 
    elif user_score > computer_score: 
        return "Your score is higher than the Opponent! You win."
    # Computer wins 
    else: 
        return "You lose! :( "

# Create a game function, this function will run so the game begins 
def playgame():
    """Function runs so the game starts"""
    print(logo) #displays the logo to begin the game 

    # Create empty lists for the user's and computer's cards, this is where the cards drawn by each 'player' are stored and how each of the above functions will make their calculations 
    user_cards = []
    computer_cards = []

    # Create a variable to notate whether the game should continue and use a Boolean value of False
    is_game_over = False
    # This will be used in conjunction with a while loop below to keep the game running as long as the value reads false 

    #Blackjack starts with two cards being dealt so we need to start the game with two cards being added to user_cards and computer_cards lists 
    # use a For Loop using the built in range() function to run the loop just twice 
    for _ in range(2):
        # Use the append method with each empty list and pass in our deal_card function 
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    #print(user_cards, computer_cards)
    # Loop runs twice, and each time our deal_card() function will output a random card. The append() method displays both values generated for each iteration in the appropriate lists. 
    # Each player is dealt two starting cards 
    # Create a while loop to "play the game" this is also known as a "game loop"
    while not is_game_over: #confirms that is it false 
        # using the calculate_score() function, create two new variables to store the scores by passing in our lists as arguments 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Using print statements and f-strings, have the current score of the user and the first card of the computer's hand display 
        # Note in BlackJack you can always see the first card dealt to your opponent but not the second one. 
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}.")

        # Create an if/else statement that states if either player has a BlackJack hand or the user goes over 21 and the game ends. 
        if user_score == 0 or computer_score == 0 or user_score > 21: 
            is_game_over = True #ends game loop 
        else: 
            user_should_deal = input("Type 'y' to get another card (hit), type 'n' to pass: ")
            # Nest an if/else statement for the outcomes of the input
            if user_should_deal == "y":
                user_cards.append(deal_card()) #deals another card and stores it in the list 
            else: 
                is_game_over = True
    # Create a while loop outside of our main game loop that keeps the computer playing as well as long as its score is not equal to 0 and under 17 
    while computer_score != 0 and computer_score < 17: 
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}. Your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}. Computer's final score: {computer_score}")
    print(compare(user_score, computer_score))
# One final while loop that takes the user's input to start or leave the program, this will also be the first thing that will show when the program is run. 

while input("Want to play BlackJack? Type 'y' to start, hit enter to leave: \n"):
    # use the clear() function we made to clear all old output and hide command line from view 
    clear() 
    # starts the game over 
    playgame() 