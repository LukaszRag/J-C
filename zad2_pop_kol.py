import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#zestaw B

dane = pd.read_csv('flags.csv', delimiter=";")
df=pd.DataFrame(dane)
print(dane)

grupa=df.groupby('Country').agg({'Religion':['sum']})
print(grupa)

grupa2=df.groupby("Landmass")
print(grupa2)

etykiety=list(grupa2.groups.keys())
wartosc=list(grupa2.agg("Country").sum())
grupa.plot(x ='Country', y='Religion', kind = 'bar')
plt.show()

