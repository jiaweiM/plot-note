# Text 概述
图文并茂，图文不分家。matplotlib 对文本支持很全面，包括数学表达式、矢量和栅格 truetype 输出、任何方向的多行文本，以及 Unicode 支持。图表的标题、坐标轴标签、legend以及额外的注释都需要文本。

matplotlib 将字体内嵌到输出文件中，如PDF 和 postscript，所以显示不会有任何变形。对 FreeType 的支持，使其可以输出漂亮的反锯齿字体，即使栅格很小也没问题。Matplotlib 内置的 `matplotlib.font_manager` 实现了跨平台、W3C兼容的字体查找算法。

matplotlib 支持对字体属性的自定义程度很高，包括 font size, font weight, text location, color 等，默认值保存在 rc 文件中。另外，Matplotlib 还实现了大量的 TeX 数学符号和命令。
