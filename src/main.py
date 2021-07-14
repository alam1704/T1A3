import os
import random
import time
import sys

import art
import emoji
import cowsay

#clear screen function
def clear():
    if os.name == "nt":
        command  = "cls"
    else:
        command = "clear"
    
    os.system(command)

#function for exiting the game.
def exit_game():
    clear()
    print("\n")
    print("Thanks for playing")
    print("\n")
    time.sleep(2)
    clear()
    exit()

#welcome screen
def welcome_screen():
    #to add the pyramid art soon... not sure if i want to add a separate function or not.
    print(art.text2art("""Who  wants 
    to  build 
    a  pyramid? """, font="medium"))
    print("\n")
    print("{:^75}".format("\u001b[4m\u001b[44m By Alex Lam \u001b[0m"))
    
#pyramid at home screen/result of the 
def pyramid_image(rows):
    row = 0 #start at row 0
    for row_num in range (1, rows+1): #for each row in the range
        for gap in range (1,(rows-row_num)+1): #for gap before text in each row in the range --> this will push the # towards the centre
            print(end="  ") # this will tell how much space to print
        while row != (2*row_num-1): 
            print("# ", end="") 
            row = row+1 # move onto the next row
        row=0
        print()
"""Need to try raise an exemption for 0 points"""

#get user name
def get_name():
    while True: #continues to ask for input until user gives a valid response.
        user_name = input("\nPlease enter a player name of less than 10 characters:\n").strip()
        if user_name == "quit":
            exit_game()
        #want only characters less than 10 to ensure leaderboard is readable.    
        elif len(user_name) > 10:
            print(f"\nSorry, \'{user_name}\' is invalid. Please try again.\nMake sure it is less than 10 characters.")
        else:
            print(f"\nWelcome {user_name}! Let's begin learning and building!\n")
            break

get_name()