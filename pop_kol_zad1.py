import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#zestaw B


x= np.arange(-2,8,0.01)
y=(np.sin(x)+np.cos(x))*x**3
plt.title("Wykres liniowy funkcji f(x)=(sin(x)+cos(x))* x3")
plt.ylabel("oś y")
plt.xlabel("oś x")
plt.xlim(-2,8)
plt.plot(x,y)
plt.show()