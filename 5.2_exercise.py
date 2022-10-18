#Maximum of number

student_scores = input("Input a list of students scores : ").split()
num =0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    #print(student_scores)
    if student_scores[n]> num:
        num = student_scores[n]
    else:
        num = num

print(f"The maximum number is : {num}")