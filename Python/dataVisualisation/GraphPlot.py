import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11)
y = 2 * x + 5
y1 = 3 * x + 5
plt.title("Line Plot")
plt.xlabel("x axis caption")
plt.ylabel("y axis caprion")
plt.xticks(np.arange(1, 11, 3))
plt.yticks(np.arange(7, 40, 1))
plt.plot(x, y)
plt.grid(color='r')
plt.plot(x, y1, 'or')
plt.show()
