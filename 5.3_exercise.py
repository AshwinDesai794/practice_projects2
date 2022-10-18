
n = int(input("Enter untill what num do you want to sum : "))

sum = 1
for num in range(2, n+1, 2):
    sum +=num
    print(num)

print(sum)