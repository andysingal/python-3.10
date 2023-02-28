#Prompt for questions and student numers
#ask from the users the number of questions and numbers of students in a class
from collections import defaultdict
import random,os
# Step 6 - Implement logic to delete all .txt files from current directory except country_data.txt
for file_name in os.listdir():
    if file_name.endswith('.txt') and not(file_name.startswith('country_data')):
        os.unlink(file_name)

question_count = int(input("How many questions will be for each quiz? "))
student_count = int(input("How many students will participate in quiz? "))

countries = defaultdict(list)
with open('country_data.txt') as country_info:
    country_info.readline()
    # country_code,country_name,capital,total_area,population, \
    #   currency_code,currency_name,lang_name = country_info.strip('\n').split(',')
    for country in country_info:
        info_list = country.strip('\n').split(';')
        name,capital = info_list[1:3]
        countries[name] = capital

#Create Question files
"""
Step 3 - Create Question Files and randomize the questions
TODO 3.1 - Generate questions files based on number of students 
TODO 3.2 - Write header for the quiz in questions text files
TODO 3.3 - Shuffle the order of countries based on random module 
TODO 3.4 - Loop through number of questions and make a question
for each
"""
for quiz_num in range(student_count):
    with open(f'questions{quiz_num + 1}.txt','w') as quiz_file:
        quiz_file.write('Name:\n\nDate:\n\n')
        quiz_file.write(f"{' '* 20} Country Capital Quiz(Form {quiz_num+1})")
        quiz_file.write('\n\n')
        #TODO 3.3 - Shuffle the order of countries based on random module
        country_list = list(countries.keys())
        random.shuffle(country_list)
        #TODO 3.4 - Loop through number of questions and make a question
        for question_num in range(question_count):
            #TODO 4
            correct_answer = countries[country_list[question_num]]
            wrong_answers = list(countries.values())
            del wrong_answers[wrong_answers.index(correct_answer)]

            #Generate answer options
            wrong_answers = random.sample(wrong_answers,3)
            answer_options = wrong_answers + [correct_answer]

            #Randomize the answer options
            random.shuffle(answer_options)

            #Write content to questions and answers text files
            # TODO 5.1 - Write questions and answer options to questions text file
            quiz_file.write(f"{question_num + 1}.What is the capital city of {country_list[question_num]}?\n")
            for i in range(4):
                quiz_file.write(f"         {'ABCD'[i]}.{answer_options[i]}\n")
            quiz_file.write('\n')
            # TODO 5.2 - Write correct answers to answers text file
            with open(f"answers{quiz_num+1}.txt","a") as answer_file:
                answer_file.write(f"{question_num+1}.{'ABCD'[answer_options.index(correct_answer)]}\n")






