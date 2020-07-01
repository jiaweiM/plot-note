import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# Setup, create data
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1, np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True

mpl.rcParams['path.simplify_threshold'] = 0.0  # no simplification
plt.plot(y)
plt.show()

mpl.rcParams['path.simplify_threshold'] = 1.0  # simplification
plt.plot(y)
plt.show()
