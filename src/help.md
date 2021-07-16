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