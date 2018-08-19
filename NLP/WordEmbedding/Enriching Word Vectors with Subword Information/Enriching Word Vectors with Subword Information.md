# Enriching Word Vectors with Subword Information


### Dictionary of n-grams：

+ 随着n-gram的引入，dict的容量也是成级数上涨，要利用hash去除一些频次较低的项，文中建议的是保留200w。


### 部分结论
+ 在越大的数据集上，embedding的维度可以适当放大。
+ 加入n-grams真的很有用，特别是数据小时，相较word2vec优势更加明显
+ 在不同语言下都比较好用，特别是那些rich language。
+ 在句法形态评估任务上效果较为显著。