import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import fsolve

def roots(file):
    x, y = np.loadtxt(file, unpack=True)
    # print(x , y)
    f = interp1d(x, y, kind='cubic')
    x0 = (-1.0, 0)
    res = fsolve(f, x0)
    print('root(s) :', res)

    xnew = np.linspace(-20, 19, num=39, endpoint=True)
    import matplotlib.pyplot as plt
    plt.plot(x, y, 'o', xnew, f(xnew), '-')
    plt.legend(['data', 'cubic'], loc='best')
    plt.show()

roots('list_points')
