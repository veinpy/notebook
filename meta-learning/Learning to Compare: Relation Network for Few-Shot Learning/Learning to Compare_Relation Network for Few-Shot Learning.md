# Learning to Compare: Relation Network for Few-Shot Learning


## 方法论
	
	1. Embedding
	2. Relation Module -> relation score
	3. 给出sample set（候选项）和query set（参照项），从候选项中选出和参照项相似分最高的那一个
	4. 通过对训练数据sampling 来选取sample set 和 query set


## 对比 Matching Net

都是metric based 方法，但是核心还是在于我们这里的重点是<mark>**学习一个metric**</mark>而不是使用现有的metric

## 对比 Siamese network

### Reference: 

[知乎](https://zhuanlan.zhihu.com/p/35379027?group_id=966092482786783232)

[paper](https://link.zhihu.com/?target=https%3A//arxiv.org/pdf/1711.06025.pdf)

[github](https://link.zhihu.com/?target=https%3A//github.com/floodsung/LearningToCompare_FSL)

---

Earlier work on few-shot learning tended to involve generative models with complex iterative inference strategies.

MAML (Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks) approach aimed to meta-learn an initial condition (set of neural weights) that is good for fine-tuning on few-shot problems.

#Learning to Compare: Relation Network for Few-Shot Learning

thie approach solves target problems in an entirely feed-forward manner with no model updates required, making it more convenient for low-latency or low-power applications.

*Training set*

*Support set*

*Testing set*

ways to exploit the training set:
	1. mimic the few-shot learning setting via episode based ttraining as proposed in [39] (训练集里拆分出suport 和test set， 从而实现训练的目的)

--
	
##Architecture:

**Embedding Module**
>	semantic embedding
>
>	拼接 sample set's embedded vector & query set's embedded vector

>	当K-shot, K>1时， training set 的每个class中K个vectors进行求和，变成一个vector

**Relation Module**
>	拼接好的vector(feature) 输入到relation module, 产出 0~1的标量，代表两者的相似度。
>
>	ri,j ， one query input xj 和 training sample set examples xi, 
>
>	consider **Relation Score** as **regression problem**, that for ground-truth we can only automatically generate \{0,1\} targets.

--

##Objective function
>	MSE