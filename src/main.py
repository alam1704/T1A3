import os
import random
import time
import sys


import art
import emoji
import cowsay

from randomizer import randomizer
from scoring import scoring, print_current_score
from leaderboard import leaderboard
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
    clear()
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
#Need to try raise an exemption for 0 points

#display menu of game
def menu():
    
    print("{:^75}".format("[1] Play Game"))
    print("{:^75}".format("[2] Display Leaderboard"))
    print("{:^75}".format("[3] Change Player Name"))
    print("{:^75}".format("[0] Exit program"))
    
    while True:
        try:
            option = int(input("Enter your option here:\n\n"))
            if option == 1:
                break
            if option == 2:
                leaderboard(score_data[1],score_data[2], user_name)  
            elif option == 3:
                get_name()#-----------------------------------------------------------
            elif option == 0:
                exit_game()
            else:
                print("INVALID INPUT, PLEASE TRY AGAIN.")
        except ValueError:
                print("INVALID INPUT, PLEASE TRY AGAIN.")

#get user name
def get_name():
    while True: #continues to ask for input until user gives a valid response.
        user_name = input("\nPlease enter a player name of less than 10 characters:\n\n").strip()
        if user_name == "quit":
            exit_game()
        #want only characters less than 10 to ensure leaderboard is readable.    
        elif len(user_name) > 10:
            print(f"\nSorry, \'{user_name}\' is invalid. Please try again.\nMake sure it is less than 10 characters.")
        else:
            print(f"\nWelcome {user_name}! Let's begin learning and building!\n")
            break

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
        print("{:^75}".format(f"Well done, you answered the question correctly"))
    else:
        print("{:^75}".format(f"Good try, unfortunately you answered the question incorrectly."))
        print("{:^75}".format(f"The correct answer was \'{current_quiz[5][i]}\'"))

#function for starting game
def start_game():
    print("\n")
    cowsay.cow("Game will start in:")
    for x in 3, 2, 1:
        print(x)
        time.sleep(1)
    print("\n\n")

#function for exiting the game.
def exit_game():
    print("\n")
    print("Thanks for playing")
    print("\n")
    time.sleep(2)
    exit()

# main application

clear() #not clearing screen - bug
welcome_screen()
pyramid_image(10)

print("{:^75}".format("Instructions"))
print("\n")
print("""-\"Who wants to build a pyramid\" is a single-player application is to allow users to learn and play a Python quiz through the terminal.
-A total of 10 questions will be selected from a pool of potential random questions starting at level 1.
-You can progress to the next level as you accumulate more points or "bricks" by answering the questions correctly.
-Level 1 questions have a value of 1 point each question, level 2 has a value of 2 points and level 3 has 3 points. 
-You need to score 3 points to move onto level 2 and 9 points to move onto level 3. 
-When prompted, type of letter of the corresponding choice to input your answer then press "Enter".
-A hidden timer will track how quickly you answer the questions.
-After each question you will be given time to review the question and answer, which will also display your current score.
-At the end of the quiz, your final score will be displayed along with how many questions you answered correctly, 
how quickly you answered the question and you finally get to see how tall you built your pyramid!
-You will be then taken back to the main menu where you can start the game again, exit or check leader board.
""")
print("\n")
print("You can exit anytime during the quiz stage by inputing \"quit\".")
print("\n")

user_name = get_name()
menu()
start_game()

answers = "a","b","c","d"
score_data = [0, 0, 0, 0]
while True:

    
    
    #score is kept as a list
    #   [0] points for current questions
    #   [1] total points
    #   [2] total time of quiz
    #   [3] total correct answers     
    
    for i in range(0, 10):
        
        if score_data[1] >= 9:
            current_quiz = randomizer(questions.level_3)
            level = 3
        elif score_data[1] >= 3:
            current_quiz = randomizer(questions.level_2)
            level = 2
        else:
            current_quiz = randomizer(questions.level_1)
            level = 1

        start_time = time.time()
        print_question(i, current_quiz, answers)
        
        user_answer = get_user_answer(answers)
        end_time = time.time()
        time_taken = "{:0.2f}".format(end_time - start_time)
        

        review_answer(i, current_quiz, answers, user_answer)

        score_data = scoring(current_quiz[5][i], user_answer, time_taken, score_data, level)

        print_current_score(score_data)

        if i + 1 != 10:
            if input("Press enter to continue to the next questions\n") == "quit":
                exit_game()
        else:
            if input("Press enter to continue to the next questions\n") == "quit":
                exit_game()
    print("\n\n")    
    print(f"Congraulations on completing the pyramid, {user_name}!\n\n")
    print(f"You anwered {score_data[3]} out of 10 questions correctly!\n")
    print(f"Your final score and the pyramid level you built up to is {score_data[1]} level(s)! Superb Work!\n")
    print(f"You only took {score_data[2]} seconds to complete the pyramid\n")
    pyramid_image(score_data[1])
    print("\n\n")

    leaderboard(score_data[1], score_data[2], user_name)
    
    menu()
    start_game()
#        """current_leaderboard = leaderboard(user_name, score_data[1], score_data[2])
#
#        if end_of_quiz_input == "l":
#            print_leaderboard(current_leaderboard)
#            end_of_quiz_input = leaderboard_input()#

#        if end_of_game_input == "y":
#            continue
#        else:
#            exit_game()"""

#keyboard interrupt exception - could instead say a "goodbye" message






