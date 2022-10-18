import random

random_integer = random.randint(0, 10)
print(random_integer)

random_float = random.random()        #random values between 0 and 1
print(random_float)

#Random number between 0 and 5
random_float_1 = random.random()* random.randint(0, 6)
#or random_float_1 = random.random() * 5
print(random_float_1)