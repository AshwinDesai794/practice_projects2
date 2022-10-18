from scipy.optimize import minimize

ar_count = []
count = 0
#n =10000
#x = 9

def Minsteps(x):

    if x == 1:
        count = 3
    #ar_count.append(count)

    while (x > 1):

        if x % 2 == 0:
            x = x / 2
            count = count + 1

        else:
            x = x * 3 + 1
            count = count + 1

    ar_count.append(count)
    print(count)

minimize(Minsteps,x0=(1,10), method='BFGS')