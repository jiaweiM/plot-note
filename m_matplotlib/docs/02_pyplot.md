# TOC
- [TOC](#toc)
- [Intro](#intro)

# Intro
matplotlib 入门的最快方法是使用它的 MATLAB 风格API (pylab)，该API和 MATLAB 的绘图函数兼容。

`matplotlib.pyplot` 在不同函数调用时，状态保持不变，它记录了当前 figure 和 plotting area，以及对当前 axes 作用的绘图函数。

pyplot 主要用于交互式绘图以及较为简单的绘图，对复杂的绘图，还是建议为面向对象 API。