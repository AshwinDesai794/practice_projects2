import time

# Start timer
start = time.time()
ar_count = []
m = 1
n = 10000

# Code to loop through each value between m and n and calculate steps required for each number
for x in range(m, n + 1):
    g = x
    count = 0

    # Code runs only if the first variable is 1, until next 1 is reached which is fixed non repeating value
    if x == 1:
        count = 3

    # Code runs for all values other than 1 in the sequence to count number of steps to reach 1
    while x > 1:
        if x % 2 == 0:
            x = x / 2
            count = count + 1

        else:
            x = x * 3 + 1
            count = count + 1

    ar_count.append(count)
    # print(count)

print(ar_count)
end = time.time()
print("Time :" + str(end - start))
