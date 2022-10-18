import numpy as np
import matplotlib.pyplot as plt

ar_count = []
m = 1
n = 10000
y = np.arange(m, n + 1)      # Creating an array of m to n with unit stepsize to to plot graph

print(y)

for x in range(m, n + 1):
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
# print(len(ar_count))
# print((len(y)))

# Code to plot the graph of steps required and unit step length
plt.title("Steps Required VS length")
plt.xlabel("Unit step size")
plt.ylabel("Steps")
# plt.xticks()
#plt.legend(y,ar_count)
plt.plot(y, ar_count)
plt.show()
