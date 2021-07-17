# Who wants to build a pyramid (WWTBAP)

## Requirements

Will need to have Python 3 installed to run the game. You can check this by running in your terminal "python3 --version" or "python --version". This was created on a MacOS system. It may not run correctly on other operating systems.

## Instructions

### Running WWTBAP through Python.

1. Open terminal on system
2. Find file path and navigate to directory of location where the file is saved, namely "main.py"
3. Enter command "python3 main.py" or "python main.py" into your terminal.

### Running WWTBAP as an executable script.

1. Open terminal on system
2. Find file path and navigate to directory location where the file is saved, namely "pyramid_game.sh". (Should be in the same directory as "main.py")
3. Enter command: 

        "./pyramid_game.sh"

4. **IF** you received the message:

    >-bash: ./pyramid_game. sh: _Permission denied_" 

continue onto step 5.

5. Confirm that the script is executable by typing in the terminal:

    >ls -l

*If the ten characters to the left of the file look like:

        "-rw-r--r--" ....

6. In the same directory, execute in the terminal:

    >chmod +x pyramid_game.sh

7. Execute the script again:

        "./pyramid_game.sh"

### Additional options - ./pyramid_game $1
You can also run the game with the following arguments on the script:

* --help: displays contents of README file instead of running application
* --install: will run pip installation without running the game

# Software Development Plan

## Statement of purpose and scope.

The initial purpose of this single-player application is to allow users to learn and play a quiz through the terminal of their computer. It is named "Who wants to build a pyramid?" inspired after the quiz game *Who wants to be a millionaire* but also *Hangman* because I wanted to make a game like Hangman but instead of penalising the player for guessing a letter wrong, the player would build a level of a 2-D pyramid for every question they got correct. The target audience was for those who were learning Python at BootCamp(like myself) and wanted to test their understanding with a more gradual learning curve compared to the intense steep learning curve of the BootCamp. 

# Features and Functions

## Menu

Upon starting the application, will be given a brief overview of the game and then the player is prompted to give a user_name. From here, the user can select from the menu how they want to proceed; play game, display leaderboard, change user name, or exit program.

## Scoring

The quiz game selects questions from a question.py file and is organised into (at the moment) **three** separate dictionaries labelled level 1, level 2, and level 3. The corresponding scores for each level are 1, 2 and 3 points. These scores are tracked throughout the game with the time taken to answer each questions. The statistics are then displayed at the end of quiz, with an ASCII art of the pyramid built and the size of pyramid built will be according to how much the player has scored. 1 point is equivalent to one level of the pyramid built.  

The quiz has also been designed so that the player is exposed to easier questions before moving onto more challenging questions. The quiz loops through level 1 questions until the player scores enough points to advance to the next level.

## Random quesitons and random order of questions

To improve replayability, the questions are selected at random, and the answers are organised in a random order. This ensures that no two quizzes are exactly the same (until of course we use all questions). The quiz uses *random.sample* to randomly select a question from a pool at the specified level. It then iterates over the answers and using the same random.sample function, it *appends* a random answer to one of the a, b, c, or d list until all lists are appended with an answer.  

## Player names and leaderboard

The idea was to have an active leaderboard stored locally on a text file, "leaderboard.txt". However, at the time of writing this readme.md, the leaderboard function is still in development. Unfortunately, this feature is still in test mode and I will continue to update this readme.md as I progress. However, the concept was to have a leaderboard function load and save to a JSON file. 

## User Interaction and Experience

The WWTBAP game was intended to be simple to use. A Menu page is set up to give user the options as described above, and they need only to answer a quiz of 10 questions to complete the game. The building of the actual pyramid is built in the background as well as the calculation of the players scores. If a user is experiencing difficulty, there is a help.md file that will run in the bash terminal after exiting the game. This file contains user instructions on how to correctly run the application on the player's operating system. Instructions and information about the game is also included with the menu at the start of the applications.

## Control Flow Diagram
#
![Control flow diagram](/docs/WWTBAP_control_flow.png)

## Implementation Plan 

For this particular project, I used Trello to assist with planning and implementing the tasks. Each part of the project was divided into their general features/functions. 

The first part of the project was to design the opening/welcome message the program would output, grab the players name and then also output a menu for the player to select how they wanted to proceed. Next it was the body part of my project which included a function that would select questions at random as well as a scoring feature for the game. Then, the leaderboard was the last feature to implement. 

All the important tasks necessary to build these functions are given a section on the Trello board, with specific goal cards created that act like building blocks for the final feature. 

![Trello 1](/docs/trello_1.png)
![Trello 2](/docs/trello_2.png)
![Trello 3](/docs/trello_3.png)
![Trello 4](/docs/trello_4.png)
![Trello 5](/docs/trello_5.png)
![Trello 6](/docs/trello_6.png)
![Trello 7](/docs/trello_7.png)
![Trello 8](/docs/trello_8.png)
![Trello 9](/docs/trello_9.png)
![Trello 10](/docs/trello_10.png)
![Trello 11](/docs/trello_11.png)
![Trello 12](/docs/trello_12.png)



