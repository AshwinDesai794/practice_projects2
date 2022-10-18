import time

start = time.time()        # Start timer
ar_count = []
m = 1
n = 10000
new_dict = dict()
f_dict = dict()

# For loop to Calculate number of steps required for each value between m and n and value in an array
for x in range(m, n + 1):
    g = x
    count = 0

    # Code runs only if the first variable is 1, until next 1 is reached which is fixed non repeating value
    if x == 1:
        count = 3

    # Code runs for all values other than 1 in the sequence to count number of steps to reach 1
    while x > 1:

        # Code to reduce redundant calculation by extracting already calculated values saved in dictionary
        if x in f_dict:
            count = count + f_dict[x]
            # print("got in loop")
            break

        elif x % 2 == 0:
            x = x / 2
            count = count + 1

        else:
            x = x * 3 + 1
            count = count + 1

    ar_count.append(count)
    new_dict = {g: count}
    f_dict.update(new_dict)         # updating dictionary to retrieve repeating Data
    # print(count)

print(ar_count)
# print(f_dict)
end = time.time()          # end timer
print("Time :" + str(end - start))
