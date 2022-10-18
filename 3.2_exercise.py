# BMI of a person

height = float(input('Enter your height in meter :'))
weight = float(input('Enter your Weight in kg :'))

bmi = weight / height ** 2

# bmi as a whole nuber
print(int(bmi))

if bmi <= 18.5:
    print("underweight")
elif bmi < 25:  # or elif 18.5<bmi<=25:
    print("normal Weight")
elif bmi < 30:
    print("overweight")
elif bmi < 35:
    print("Obese")
else:
    print("Clinically Obese")
