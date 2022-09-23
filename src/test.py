import matplotlib.pyplot as plt
import matplotlib.axes._axes as axes
import matplotlib.figure as figure
import numpy as np


def relu(x):
    return np.where(x < 0, 0, x)


def relu_derivative(x):
    return np.greater(x, 0).astype(int)


xs = np.arange(-5, 6)

fig, (ax1, ax2) = plt.subplots(2, 1)  # type:figure.Figure, (axes.Axes, axes.Axes)

ax1.plot(xs, relu(xs), linewidth=2.4)
ax1.set_aspect('equal', adjustable='box', anchor='C')

ax2.plot(xs, relu_derivative(xs), linewidth=2.4)
ax2.set_aspect('equal', adjustable='box', anchor='C')

plt.tight_layout()
plt.show()
