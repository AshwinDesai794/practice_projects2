# Dictionary Comprehension
import random

name_list = ['Aex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

students_scores = {student : random.randint(0,100) for student in name_list}

print(students_scores)

# passsed_students = {new_key: new_value for (key, new_value) in dictionary.items()}    #formula

passsed_students = {student: score for (student, score) in students_scores.items() if score >= 60}

print(passsed_students)