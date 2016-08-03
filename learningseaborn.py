#Author: Alan Izar
#Trying to understand matplotlib and seaborn

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(sum(map(ord,"aesthetics")))

def sinplot(flip=1):
    x = np.linspace(0,14,100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * 0.5) * (7 - i) * flip)
    plt.show()

sns.set_style("white")

sinplot()

with sns.axes_style("darkgrid"):
    plt.subplot(211)
    sinplot()
plt.subplot(212)
sinplot(-1)