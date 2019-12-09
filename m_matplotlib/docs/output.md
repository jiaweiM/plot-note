# 介绍

matplotlib 通过 `pyplot.savefig()` 输出图片，该方法通过保存文件名的后缀确定导出文件类型。
- 如果没有后缀，默认导出为 svg 格式。
- 如果后缀对应的格式不支持，抛出异常。

支持格式：
- PNG，相对JPEG，PNG允许使用透明背景色。
- PDF
- SVG
- Post (Postscript)，适合于图像批量处理用于发布。

# Figure.savefig
保存当前 figure.

调用方法：
```py
savefig(fname, dpi=None, facecolor='w', edgecolor='w',
        orientation='portrait', papertype=None, format=None,
        transparent=False, bbox_inches=None, pad_inches=0.1,
        frameon=None, metadata=None)
```
输出格式取决于使用的后端。

**fname**

`str`、`Path` 或 `file` 对象。

如果未设置 `format`

**format**

`str` 类型。

# 分辨率
分辨率说明了对图片细节记录的详细程度，衡量图片放大多少不会失真，高分辨率的图片，在较大尺寸时依然能保持高质量，但是其文件也更大。

分辨率通过每英寸像素点的数目来衡量（number of color pixel dot per inch, dpi）。

**PPT 分辨率**

|Screen height (pixel)|Resolution|
|---|---|
|720	|96 (default)|
|750	|100|
|1125	|150|
|1500	|200|
|1875	|250|
|2250	|300|

**Poster 分辨率**：300 dpi+

**Web**: 72 dpi+ (推荐SVG)