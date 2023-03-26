import numpy as np
from matplotlib import pyplot as plt
from scipy import optimize
def Funct(x):
    
    Valz = np.sin(2*x**2)
    return Valz



x0 = 0
fun = lambda x: np.sin(2*x**2)
res = optimize.minimize(fun, x0, method='Nelder-Mead')
print(res)

ran = 2
x0 = np.arange(.1, ran, 0.01)
values = [Funct(i) for i in x0]
mv  = x0[values.index(min(values))] 

plt.plot(x0, values, label = "Function")
plt.grid()
plt.title('My Function with the minimum')
plt.ylabel('f(x)')
plt.xlabel('x-values')
plt.axvline(mv, color = 'r', label = "location of Minimum on x-axis")
plt.legend()

plt.show()
