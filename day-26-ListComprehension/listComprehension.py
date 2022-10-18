num = [1, 2, 3, 4, 5]

# new_list = [new_item for itein list]    #formula
new_list = [n+1 for n in num]

print(new_list)

name = "Ashwin"

letters_list = [letter for letter in name]

print(letters_list)

num_to_double = [2*n for n in range(1,5)]
print(num_to_double)

name_list = ['Aex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'Freddie']

short_names = [name.upper() for name in name_list if len(name) < 5]
print(short_names)