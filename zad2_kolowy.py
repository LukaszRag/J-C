import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dane=pd.read_excel("mieszkania2.xlsx" )
dane=pd.DataFrame(dane)
print(dane)

dozadania=dane[dane["Rok"]==2015]
print(dozadania)
plt.pie(dozadania["Wartość"],labels=dozadania["Formy budownictwa"])
plt.title("Wartości poszczególnych form budownictwa w 2015 roku.")
plt.legend(loc="lower left")
plt.annotate("165940",[-1,1])
plt.savefig("zad2.pdf", format="pdf")
plt.show()