#for loop
'''
fruits = ["Aple", "Peach", "Pear"]

for fruit in fruits:      #for each loop
    print(fruit)
    '''

# Average Height without using sun() and len() function
sum = 0
num = 0
student_heights = input("Enter Student heights : ").split()   #split at spaces
for n in range(0, len(student_heights)):                      #range is 0 to excluding last number
    student_heights[n] = int(student_heights[n])
    sum = sum + student_heights[n]
    num = num+1
print(student_heights)

avg = sum/num                                                   #len(student_heights)
print(f"Average is : {avg}")

