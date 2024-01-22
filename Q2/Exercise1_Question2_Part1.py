"""_NOTE_
You need to complete those part denoted by "???"
"""
import numpy as np
from scipy.stats import ??? # what function should be imported to create a normal distribution?
import matplotlib.pyplot as plt

mu_set1 = ???
sigma1 = ???
sigma2 = ???
sigma3 = ???

sigma_set2 = ???
mu1 = ???
mu2 = ???
mu3 = ???

x = np.linspace(-10, 10, num=1000)

dist1 = ???(mu_set1, sigma1)
dist2 = ???(mu_set1, sigma2)
dist3 = ???(mu_set1, sigma3)

dist4 = ???(mu1, sigma_set2)
dist5 = ???(mu2, sigma_set2)
dist6 = ???(mu3, sigma_set2)

dist1_pdf = dist1.???(x)#What function should be used to calculate the "probability density"?
dist2_pdf = dist2.???(x)
dist3_pdf = dist3.???(x)
dist4_pdf = dist4.???(x)
dist5_pdf = dist5.???(x)
dist6_pdf = dist6.???(x)

fig, (ax1, ax2) = plt.subplots(2,1)
ax1.set_ylabel("probability")
ax1.set_xlabel("x")
ax1.plot(x, ???, 'r', label="mu=0, sigma=0.1")
ax1.plot(x, ???, 'g', label="mu=0, sigma=0.3")
ax1.plot(x, ???, 'b', label="mu=0, sigma=0.7")
ax1.set_title(label='Set 1')
ax1.legend()

ax2.set_ylabel("probability")
ax2.set_xlabel("x")
ax2.plot(x, ???, 'r', label="mu=-5, sigma=0.5")
ax2.plot(x, ???, 'g', label="mu=0, sigma=0.5")
ax2.plot(x, ???, 'b', label="mu=5, sigma=0.5")
ax2.set_title(label='Set 2')
ax2.legend()

plt.show()


### Briefly explain your understanding hereunder.
???