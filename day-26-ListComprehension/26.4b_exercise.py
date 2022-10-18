sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# passsed_students = {new_key: new_value for (key, value) in dictionary.items()}
new_sentence = sentence.split()
print(new_sentence)
print(len(new_sentence[2]))
# students_scores = {student : random.randint(0,100) for student in name_list}
result = {word: len(word) for word in new_sentence}           #instead of new sentence sentence.split() can be written


print(result)