# Matching Networks for One Shot Learning

Matching Net, which utilize attention and memory that enable rapid learning.

Machine Learning principle: test and train conditions must match.

Combine non-parametric and parametric approach.

Cast the problem of one-shot learning within the set-to-set framework.

matching network produce sensible test labels for unobserved classes without any changes to the network.

**Figure1. Matching Networks architecture**

**eq 1.**
the output for a new class is a linear combination of the labels in the support set.

the estimation for y_hat label is Akin to kernel density estimator.


使用可称为attention的函数计算新输入x_hat与memory中的sample的距离，实现对sample所对应的label进行加权处理。 
实现上，label数据是one-hot labeling，因此它无法做到在种类增加的情况下来one-shot learning。另外training的细节依然较为模糊

[reference_blog](https://blog.acolyer.org/2017/01/03/matching-networks-for-one-shot-learning/)