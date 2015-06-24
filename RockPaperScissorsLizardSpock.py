# Rock-Paper-Scissors-Lizard-Spock Game


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors



# helper functions

import random

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2

    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else :
        print "Wrong Input"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else :
        print "Wrong Input"
    
    

def rpsls(player_choice): 
    print ""
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    computer_number = random.randrange(0,5)
    computer_choice = number_to_name(computer_number)
    print "Computer chooses " + computer_choice
    diff = (player_number - computer_number) % 5
    if diff==1 or diff==2 :
        print "Player wins!"
    elif diff==3 or diff==4 :
        print "Computer wins!"
    else :
        print "Player and Computer ties!!"


flag=1    
print "Welcome to Rock-Paper-Scissors-Lizard-Spork"
while flag==1:
    print "Enter your Choose (rock,paper,scissors,lizard or Spock)"
    rpsls(raw_input())
    print "Do you wish to play again? (Yes or No)"
    reply = raw_input()
    if reply=="No":
        flag=0
        print "Thank You for Playing "
        
    

