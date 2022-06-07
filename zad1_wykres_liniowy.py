import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-6,6.8,0.1)
b=(20*np.sin(x))
c=((2*x/5)-2)
d=(7-x)

plt.plot(x,b,"r--",label="y=20*sin(x)")
plt.plot(x,c,"y--",label="y=(2x/5)-2")
plt.plot(x,d,"g-",label="y=7-x)")
plt.legend(loc="lower left")
plt.title("Tytuł ABCD")
plt.ylim(-30,30)
plt.xlim(-6.8,6.8)
plt.savefig("zad1.png", format="png")
plt.show()
