# matplotlib.pyplot.savefig

## 简介

```python
matplotlib.pyplot.savefig(*args, **kwargs)
```

保存当前 figure。调用：

```python
savefig(fname, *, dpi='figure', format=None, metadata=None,
        bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto',
        backend=None, **kwargs
       )
```

可用的输出格式取决于使用的 backend。

参数：

- **bbox_inches**`：str` or `Bbox`，默认 `rcParams["savefig.bbox"]` (默认 `None`)

边界框（bounding box），以英寸为单位：只保存 figure 的一部分。'tight' 表示只保存 figure 

## 参考

- https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
