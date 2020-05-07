# Hierarchical Clustering

- [Hierarchical Clustering](#hierarchical-clustering)
  - [简介](#%e7%ae%80%e4%bb%8b)
  - [相似度方法](#%e7%9b%b8%e4%bc%bc%e5%ba%a6%e6%96%b9%e6%b3%95)
    - [Single Linkage (Nearest neighbor)](#single-linkage-nearest-neighbor)
    - [Complete Linkage](#complete-linkage)
    - [Average Linkage](#average-linkage)

## 简介

假设有 N 个待聚类的样本，分层聚类步骤：

1. 将每个样本归为一类，计算每两个类之间的距离，即样本与样本之间的相似度；
2. 寻找最近的两个类，将它们归为一类，总类别数减一；
3. 重新计算生成的这个类和其它类之间的相似度；
4. 重复2和3直到所有样本点归为一类，聚类结束

整个聚类过程就是建立一棵树的过程，在聚类过程中，可以在第二步上设置一个阈值，当最近的两个类的距离大于该阈值，迭代终止。

第三步比较关键，如何判断两个类之间的相似度有多种方法。

## 相似度方法

### Single Linkage (Nearest neighbor)

取两个类中距离最近的两个样本的距离作为这连个集合的距离，即最近的两个样本之间的距离越小，这两个类之间的相似度就越大。

这种方法容易造成 Chaining 效应，即两个 cluster 离的比较远，但由于其中个别点距离较近就被合并了，这样合并之后 Chaining 效应会进一步扩大，最后得到比较松散的 Cluster。

### Complete Linkage

这个是 Single Linkage 相对的另一个极端，取两个集合中距离最远的两个点作为两个集合的距离。其效果也刚好相反，两个 cluster 即使已经很接近了，但是只要有不配合的点存在，就不合并。

### Average Linkage

把两个集合中两两点的距离全部取平均值，能得到更合适的结果。

该方法的一个变种是取中值，中值相对均值，受个别异常值的影响较小。
