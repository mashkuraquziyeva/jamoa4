import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

un = pd.read_csv('u.csv')
yil = un['year']
teach = un["teaching"]
plt.plot(yil, color="DarkBlue", label="Yil")
plt.plot(teach, color="Blue", label="O'quv")
un["teaching"].plot(kind='hist')
plt.legend()
plt.title("Yillari")
plt.show()
print(un)
