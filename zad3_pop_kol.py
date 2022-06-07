import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#zestaw B

dane = pd.read_csv('flags.csv', delimiter=";")
df=pd.DataFrame(dane)
print(dane)
grupa=df.groupby('Zone').agg({'Population':['sum']})
etykiety = list(grupa.groups.keys())
wartosc= list(grupa.agg('Population').sum())
print(grupa)

plt.pie(x=etykiety,labels=wartosc, autopct='%.2f %%')
plt.title("Ludność w strefach świata")
plt.legend(loc="best")
plt.show()




