import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

fig, ax = plt.subplots(1, 1)

np.random.seed(42)

N = 100
p = 0.21
mean, var, skew, kurt = binom.stats(N, p, moments='mvsk')

x = np.arange(binom.ppf(0.01, N, p), binom.ppf(0.99, N, p))

y = binom.pmf(x, N, p)

# convert frequency of heads --> θ 
x = [theta / 100 for theta in x] 

ax.plot(x, y, marker=".", ms=6, label='binom pmf', color="r")

plt.xlim(0, 1)
plt.title('Probability density function for frog tosses')
plt.xlabel('θ')
plt.ylabel('Probability')
plt.show()