
# 简介
Plotly Express 是一个包装 plotly.graph_objects 的简洁高级API，以快速实现数据搜索和生成 figure.

# 导入
下面导入 plotly.express，其中含有内置的数据集，如：
```py
import plotly.express as px

print(px.data.iris().head())
```
输出为：
```
   sepal_length  sepal_width  petal_length  petal_width species  species_id
0           5.1          3.5           1.4          0.2  setosa           1
1           4.9          3.0           1.4          0.2  setosa           1
2           4.7          3.2           1.3          0.2  setosa           1
3           4.6          3.1           1.5          0.2  setosa           1
4           5.0          3.6           1.4          0.2  setosa           1
```

# Scatter and Line plots


# Reference
- https://plot.ly/python-api-reference/plotly.express.html

