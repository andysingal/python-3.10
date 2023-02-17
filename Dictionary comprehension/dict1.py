import random
nomi = ['Alex','Beth','Caroline','Dave','Freddie']

student_scores = {student:random.randint(1,100) for student in nomi}

passed_student = {name:score for name,score in student_scores.items() if score >= 60}

print(passed_student)