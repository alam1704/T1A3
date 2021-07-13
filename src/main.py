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
    time.sleep(3)
    clear()
    exit()

#welcome screen
def welcome():
    #to add the pyramid art soon... not sure if i want to add a separate function or not.
    print(art.text2art("""Who  wants 
    to  build 
    a  pyramid? """, font="pyramid"))
    

