import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

x=np.arange(0,30.02,0.1)
a=np.sin(x)
b=np.cos(x)

plt.subplot(2,1,1)
plt.plot(a,"r:",label="sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres sin(x)")
plt.subplot(2,1,2)
plt.plot(b, "bo",label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres cos(x)")
plt.savefig("2wykresy.png")
im1 = Image.open("2wykresy.png")
im1 = im1.convert("RGB")
im1.save("2wykresy.png")

plt.subplots_adjust(hspace=0.5)
plt.show()