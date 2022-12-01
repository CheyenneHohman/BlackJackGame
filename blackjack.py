from art import logo 

import os
import random 

def clear():
    """Clears the console""" 
    command = 'clear'

    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
    card = random.choice(cards)
    return card 

def calculate_score(cards):
    """Takes a list of cards and returns the total score calculated. Keeps score as user plays the game"""
    if sum(cards) == 21 and len(cards) == 2: 
        return 0
    if 11 in cards and sum(cards) > 21: 
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score): 
    """Pass in user & computer scores as arguments"""
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

def playgame():
    """Function runs so the game starts"""
    print(logo) #displays the logo to begin the game 

    user_cards = []
    computer_cards = []

    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21: 
            is_game_over = True #ends game loop 
        else: 
            user_should_deal = input("Type 'y' to get another card (hit), type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card()) 
            else: 
                is_game_over = True
    while computer_score != 0 and computer_score < 17: 
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}. Your final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}. Computer's final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Want to play BlackJack? Type 'y' to start, hit enter to leave: \n"):
    # use the clear() function we made to clear all old output and hide command line from view 
    clear() 
    # starts the game over 
    playgame() 