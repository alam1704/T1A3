import os
import random
import time
import sys


import art
import emoji
import cowsay

from randomizer import randomizer
from scoring import scoring, print_current_score
import questions

#clear screen function
def clear():
    if os.name == "nt":
        command  = "cls"
    else:
        command = "clear"
    
    os.system(command)

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

#display menu of game
def menu():
    print("[1] Play Game")
    print("[2] Display Leaderboard")
    print("[3] Get Help")
    print("[0] Exit program")

# prints the question
def print_question(question_number, quiz_data, answers):
    print(f"{current_quiz[0][i]}\n")

    # iterate over choices to print each one
    for x in range(0, len(answers)):
        print(f"    {answers[x]}) {current_quiz[x + 1][i]}")

    print("\n")

#get user answer
def get_user_answer(answers):
    while True: 
        user_answer = input("Enter you answer: ").strip().lower()
        if user_answer in answers:
            break
        else:
            print("Sorry, this is not on of the 4 choices, please try again.")

    return user_answer

#review answer from user input
def review_answer(question_number, quiz_data, answers, user_answer):
    if user_answer == current_quiz[5][i]:
        print(f"        Well done, you answered the question correctly")
    else:
        print(f"        Good try, unfortunately you answered the question incorrectly.")
        print(f"        The correct answer was \'{current_quiz[5][i]}\'")

#function for exiting the game.
def exit_game():
    clear()
    print("\n")
    print("Thanks for playing")
    print("\n")
    time.sleep(2)
    clear()
    exit()

# main application
clear() #not clearing screen - bug
welcome_screen()
pyramid_image(10)
user_name = get_name()
print("\n")
while True:

    answers = "a","b","c","d"
    
    #score is kept as a list
    #   [0] points for current questions
    #   [1] total points
    #   [2] total time of quiz      
    score_data = [0, 0, 0]
    #in case library of questions is < number of questions being asked in quiz; I included an exception for a ValueError.
    
    try:
        if score_data[1] > 5:
            current_quiz = randomizer(questions.level_2) # this will give a ValueError if Sample is larger than population of questions.
        else:
            current_quiz = randomizer(questions.level_1)
    except ValueError:
        print("Not enough questions in question.py file, please add more before continuing.")
        print("Or change the number_of_questions you would like to be asked in the randomizer.py")
        break
    

    for i in range(0, len(current_quiz[0])):

        start_time = time.time()
        print_question(i, current_quiz, answers)
        
        user_answer = get_user_answer(answers)
        end_time = time.time()
        time_taken = end_time - start_time

        review_answer(i, current_quiz, answers, user_answer)

        score_data = scoring(current_quiz[5][i], user_answer, time_taken, score_data)

        print_current_score(score_data)

    break

#keyboard interrupt exception - could instead say a "goodbye" message






