import matplotlib.pyplot as plt
import matplotlib.axes._axes as axes
import matplotlib.figure as figure
import numpy as np

t = np.arange(0.01, 5.0, 0.01)
s = np.exp(-t)

fig, ax = plt.subplots()  # type:figure.Figure, axes.Axes

ax.plot(t, s)
ax.set_xlim(5, 0)  # decreasing time
ax.set_xlabel('decreasing timee (s)')
ax.set_ylabel('voltage (mV)')
ax.set_title('Should be growing...')
ax.grid(True)
plt.show()
