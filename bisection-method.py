import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def f(x):
    return x**2 - 2

# method bisection
def bisection(a,b,tol):
    xl = a
    xr = b
    i = 1
    while (np.abs(xr-xl)>= tol):
        c = (xl + xr)/2.0
        fung = f(xl)*f(c)
        if fung > tol:
            xl = c
            i += 1
        else:
            if fung < tol:
                xr = c
                i += 1
    return i,c

jawaban = bisection(-5,5, 1e-8)
print('jawaban = ', jawaban[1])
print('jumlah iterasi = ', jawaban[0])

# menggunakan libray scipy
jawaban = fsolve(f,[-5,1.5])
print ('hasil menggubakan fsolve untuk menemukan root = ', jawaban[0])

x = np.linspace(-2,2,100)
plt.plot(x, f(x))
plt.grid()
plt.show()
