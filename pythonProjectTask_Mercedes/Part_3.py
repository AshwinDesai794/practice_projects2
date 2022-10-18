from scipy.optimize import minimize
import scipy
ar_count = []
m = 1
n =10000



def Minsteps(x):
    count = 0
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
    #print(count)

for x in range(m, n+1):
    count = 0
    #Minsteps(x)
    #res = scipy.optimize.least_squares(Minsteps(x), x, jac='2-point', method='trf', ftol=1e-08, xtol=1e-08, gtol=1e-08, x_scale=1.0, loss='linear', f_scale=1.0, diff_step=None, tr_solver=None, tr_options={}, jac_sparsity=None, max_nfev=None, verbose=0, args=(), kwargs={})
    result = minimize(Minsteps(x), [1,1], method="BFGS", bounds=[1,100],  options={"eps":eps, "disp":True})

print(ar_count)
#result = minimize(Minsteps)