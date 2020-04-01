# %%[markdown]
# First we load and configure the libraries we need:
# %%
import numpy as np
import matplotlib.pyplot as plt

# Make numpy print 4 significant digits for prettiness
np.set_printoptions(precision=4, suppress=True)
np.random.seed(5)

# %%[markdown]
# Here is a set of data, made out of random numbers, that we will use as a pretend time series, 
# or a single line of data from one plane of an image.


# %%
n_points = 40

x_vals = np.arange(n_points)
y_vals = np.random.normal(size=n_points)
plt.bar(x_vals, y_vals)

# %%[markdown]
# ## The Gaussian kernel
# The ‘kernel’ for smoothing, defines the shape of the function that 
# is used to take the average of the neighboring points. A Gaussian 
# kernel is a kernel with the shape of a Gaussian (normal distribution) 
# curve. Here is a standard Gaussian, with a mean of 0 and a 
# σ (=population standard deviation) of 1.


# %%
x = np.arange(-6, 6, 0.1)  # x from -6 to 6 in steps of 0.1
y = 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2.)
plt.plot(x, y)


# %%[markdown]
# In the standard statistical way, we have defined the width of the 
# Gaussian shape in terms of σ. However, when the Gaussian is used 
# for smoothing, it is common for imagers to describe the width of 
# the Gaussian with another related measure, the Full Width at Half 
# Maximum (FWHM).
#
# The FWHM is the width of the kernel, at half of the maximum of the 
# height of the Gaussian. Thus, for the standard Gaussian above, the 
# maximum height is ~0.4. The width of the kernel at 0.2 (on the Y axis) 
# is the FWHM. As x = -1.175 and 1.175 when y = 0.2, the FWHM is roughly 2.35.
#
# The FWHM is related to sigma by the following formulae (in Python):

# %%
def sigma2fwhm(sigma):
    return sigma * np.sqrt(8 * np.log(2))


def fwhm2sigma(fwhm):
    return fwhm / np.sqrt(8 * np.log(2))

