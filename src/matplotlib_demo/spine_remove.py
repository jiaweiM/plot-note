import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)

fig, ax = plt.subplots()

ax.plot(x, x, label="linear")

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")

plt.legend()
plt.show()
