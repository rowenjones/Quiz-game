import requests
#import random to randomise multiple choice answers
import random
#import statistics to work out mode of winners
import statistics

#function to get the questions and answers from the API
def get_questions():
    parameters = {
        "amount": 10,
        "type": "multiple"
    }

    response = requests.get(url="https://opentdb.com/api.php?amount=10", params=parameters)
    question_data = response.json()["results"]
    return question_data

#function to run the quiz for more than one player
def run_quiz(player_name):

#starting score is 0
    score = 0

#Call the function to get the questions and answers
    questions = get_questions()

#Explain the game to the players
    print(f"Welcome to this general knowledge quiz. This is a 2 player game. There will be ten multiple choice questions, and you will get your results at the end.")

#For each question print the question with a number starting from 1
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        possible_answers = question["incorrect_answers"] + [question["correct_answer"]]
#Randomise the answers
        random.shuffle(possible_answers)

#Print the possible answers with numbers from 1
        for j, option in enumerate(possible_answers, 1):
            print(f"{j}. {option}")

#User puts in the number of the answer they want to guess
        guessed_answer = input("Enter the number of your answer from 1 to 4: ")

#Convert the number guessed to an integer and take away 1 to obtain the index in the list
        if possible_answers[int(guessed_answer) - 1] == question["correct_answer"]:
            print("Correct!\n")

#Add 1 to the score
            score += 1
        else:
            print(f"Incorrect this time. The correct answer was: {question['correct_answer']}\n")

#Show the score for the player
    print(f"{player_name}, you got {score}/{len(questions)} questions correct.")
    return score

#Get an input for the player's name - to lower case to ensure comparrison later
name_1 = input("Player 1: What is your name?").lower()
#Run the quiz for the first player
score_1 = run_quiz(name_1)

#Get an input for the second player's name - to lower case to ensure comparrison later
name_2 = input("Player 2: What is your name?").lower()
#Run the quiz for the second player
score_2 = run_quiz(name_2)

#Work out which player has won
if score_1 > score_2:
    print(f"Player 1 wins, well done {name_1}")
    file = open('Winners.txt', 'a+')
    file.seek(0)
    file.write(name_1 + '\n')
    file.close()
elif score_2 > score_1:
    print(f"Player 2 wins, well done {name_2}")
    file = open('Winners.txt', 'a+')
    file.seek(0)
    file.write(name_2 + '\n')
    file.close()
else:
    print("It was a draw")

#Work out the overall winner from a few games
file = open('Winners.txt', 'r')
data = file.read()
#Convert the text file into a list
winners = data.replace('\n', ',').split(",")
file.close()
#Work out the string which occurs the most
overall_winner = statistics.mode(winners)
print(f"Well done {overall_winner}, you have won the most games and are the overall winner.")
