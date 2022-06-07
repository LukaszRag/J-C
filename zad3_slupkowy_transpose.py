import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane=pd.read_excel("turystyka2.xlsx", header=None )
dane=pd.DataFrame(dane)
print(dane)
dane2=dane.transpose()
dane3 = dane2.rename({0: 'Kategoria', 1: 'Rok', 2: 'Ilość'}, axis='columns')
print(dane3)

k1=dane3[dane3["Kategoria"]=="kategorii *"]
k2=dane3[dane3["Kategoria"]=="kategorii **"]
k3=dane3[dane3["Kategoria"]=="kategorii ***"]
k4=dane3[dane3["Kategoria"]=="kategorii ****"]
k5=dane3[dane3["Kategoria"]=="kategorii *****"]

x=np.arange(0,6)
plt.bar(x-0.20,k1["Ilość"], width=0.10, label="kategorii *")
plt.bar(x-0.10,k2["Ilość"], width=0.10, label="kategorii **")
plt.bar(x,k3["Ilość"], width=0.10, label="kategorii ***")
plt.bar(x+0.10,k4["Ilość"],width=0.10, label="kategorii ****")
plt.bar(x+0.20,k5["Ilość"], width=0.10, label="kategorii *****")
plt.legend()
plt.xticks(x, k1["Rok"])
plt.xlabel("Rok")
plt.ylabel("Ilość")
plt.title("Udział różnych kategorii hoteli w poszczególnych latach:")
plt.annotate("165940",[-1,1])
plt.savefig("zad2.png", format="png")
plt.show()

