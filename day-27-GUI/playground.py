def add(*args):
    # print(args)
    sum = 0
    for n in args:
        sum += n
    return sum

x= add(3, 5, 6)
print(x)

def calculate(**kwargs):
    print(kwargs)
    print(kwargs["multiply"])

calculate(add=3, multiply=5)
