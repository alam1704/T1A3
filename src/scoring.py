#calculate the score based on the level of the question asked --> return value
#score data from previous question is passed onto the function as a list. 
#score is kept as a list
    #   [0] points for current questions
    #   [1] total points
    #   [2] total time of quiz
    #   [3] total correct answers      
    #score_data = [0, 0, 0]

def scoring (answer, user_answer, time_taken, score_data, level):
    score_data[0] = 0
    if answer == user_answer:
        score_data[0] += 1*level
        score_data[1] += score_data[0] # adds current points to total points.
        score_data[2] += time_taken
        score_data[3] += 1
    return score_data

def print_current_score(score_data):
    print("\n----------------------------------------------\n")
    print(f"You current score is {score_data[1]}\n")