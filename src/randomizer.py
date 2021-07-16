import random
import questions
# takes the question dictionary for the selected topic and randomly picks questions and 4 choices for each
# returns a list of lists containing the questions, choices and the answer key

def randomizer(question_dict):
    number_of_questions = 10

    #create individual empty list to hold corresponding selections
    question_list = []
    a_list = []
    b_list = []
    c_list = []
    d_list = []
    answer_key = []

    #picks random question from dictionary passed onto function
    random_questions = (random.sample(list(question_dict), k=number_of_questions))

    for question in random_questions:
        random_selection = random.sample(list(question_dict[question]["answers"]), k=4)
        #to select 3 other random answers

        #then add the values to the empty list created above 

        question_list.append(question_dict[question]["question"])
        a_list.append(question_dict[question]["answers"][random_selection[0]])
        b_list.append(question_dict[question]["answers"][random_selection[1]])
        c_list.append(question_dict[question]["answers"][random_selection[2]])
        d_list.append(question_dict[question]["answers"][random_selection[3]])

    #once list  of answers for each question is populated, iterate over list which answer is correct and create answer key.

    for i in range(0, len(random_questions)):
        if a_list[i] == question_dict[random_questions[i]]["answers"]["correct"]:
            answer_key.append("a")
        elif b_list[i] == question_dict[random_questions[i]]["answers"]["correct"]:
            answer_key.append("b")
        elif c_list[i] == question_dict[random_questions[i]]["answers"]["correct"]:
            answer_key.append("c")
        elif d_list[i] == question_dict[random_questions[i]]["answers"]["correct"]:
            answer_key.append("d")
        else:
            answer_key.append("answer not found")

    return [question_list, a_list, b_list, c_list, d_list, answer_key]

        

            
