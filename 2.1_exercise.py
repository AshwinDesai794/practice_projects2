print("\nWelcome to the Tip Calculator \n")

total_bill = float(input('TOtal Bill :'))
no_people = float(input('How many people to split the bill : '))
tip_percent = float(input('What percentage of tip would you like to give: '))

bill_PerPerson = ((total_bill / no_people) + ((total_bill * (0.01 * tip_percent)) / no_people))

final_bill = round(bill_PerPerson, 2)
final_bill = "{: .2f}".format(final_bill)  # adds zero until 2 decimal places if no digit
print('Each person Should Pay: ', str(final_bill))

# print(type(no_people))
