## Model Compression and Knowledge Distillation

### 各类操作
+ Parameter pruning and sharing
	+ model quantization
	+ model binarization
	+ structural matrices
	+ parameter sharing
+ Low-rank factorization
	+ matrix decomposition
+ Transferred compact convolutional filters
	+ compress convolutional filters 
+ Knowledge distillation
	+ <mark>**large model to small model**</mark>

----
### Model Quantization
通过改变模型计算的数值精度，降低模型所需算力，从而提升性能。

模型实现tutorial：  
[**tf tutorial**](https://www.tensorflow.org/performance/quantization)  
[**pytorch tutorial**](https://pytorch.org/docs/stable/quantization.html)

经过简单的测试，pytorch的方法，直接quantize且不用finetune效果也能接受（也可能跟模型本身有关系）

----
### Knowledge Distillation
**Motivation**: over parameterization improves the generalization performance.

Three key components:

+ knowledge
+ distill algorithm
+ teacher-student architecture

Extended topics:

+ teacher-student learning
+ mutual learning
+ assistant teaching
+ lifelong learning
+ self-learning

Extend to transfer learning:

+ dataset distill: 
	+ transfers the knowledge from a large dataset into a small dataset to reduce the training loads of deep models
+ adversarial attacks
+ data augmentation
+ data privacy and security

Successful distillation relies on <I>**data geometry**</I>, <I>**optimization bias of distillation objective**</I> and <I>**strong monotonicity of the student classifier**</I>.<font color="blue">[[1]](#[1])</font>

Emprirical results show that a larger model may not be a better teacher because of model capacity gap.<font color="blue">[[2]](#[2])</font>

Experimens also show taht distillation adversely affects the student learning.<font color="blue">[[3]](#[3])</font>

#### Knowledge Representation

factors includes: 

+ activation
+ neurons' output

**Methods**:

+ **mimic final prediction(logits)** of teacher model
	+ space distance, like: cross-entropy, MSE, cosine
+ **mimic final probability**(soft-target:softmax) of teacher model
	+ distribution divergences, like: KL
+ **feature learning**(intermediate layers)（<I>teacher-student中间层的差异包括：层数、层大小、激活函数、算子类型；如何较好的方式使用并产生效果是一个突破点</I>）
	+ direct feature match
	+ indirect feature match (各类可解释的因子)
		+ derive attention map from original feature map
+ **mimic mutual-info flow from pairs of hint layers**（teacher模型层间的关系知识学习并用来教育student）
	+ graph based KD: intra-data relations between any two feature maps (via multi-head attention network)
+ **mimic instance-level mutual-info**
	+ instance feature embedding
	+ similarity between instance pairs

---
#### Knowledge Training Schema

three main categories:

+ offline distillation
+ online distillation
+ self-distillation

这个后面继续看

---
#### Student Structure

classic methods for student structure optimization:

+ Simplified Structure
	+ fewer layers and fewer channels
+ Quantized Structure
+ Small Network with efficient basic operations
+ Small Network with optimized global network structure
	+ ✨NAS, searching efficient meta operations or blocks
	+ dynamically removig redundant layers in a data-driven way using RL
+ Same Network

---

#### Algorithms

+ Adversarial Distillation
	+ (a)
	+ (b)
	+ (c)
+ Multi-Teacher Distillation
+ Cross-Modal Distillation
+ Graph-based Distillation
	+ graph as carier of teacher knowledge
	+ use graph to control the message passing of the teacher knowledge
+ 🌟Attention-Based Distillation
	+ [medium tutorial](https://tzuruey.medium.com/attention-is-all-you-need-98d26aeb3517)
+ Quantized Distillation
+ Lifelong Distilaltion
	+ continual learning
	+ continuous learning
	+ meta-learning
	+ <I>keyproblem: catastrophic forgetting</I>
+ NAS-based Distillation

---
#### In my mind, 

**Composite Teacher Model**

对于一个系统，单纯的End2End模型并不适用于

**measure the student model's capacity**

**is single loss enough**
multi-bp strategy 是否有前景

**collaborative learning**<font color="blue">[[4]](#[4])</font>

explore diverse knowledge transfer patterns

---
Reference:  

[1] <a name="[1]">Phuong, M. & Lampert, C. H. (2019a). Towards understanding knowledge distillation. In: ICML</a>  

[2] <a name="[2]">Mirzadeh, S. I., Farajtabar, M., Li, A. & Ghasemzadeh, H. (2020). Improved knowledge distillation via teacher assistant. In: AAAI.</a>  

[3] <a name="[3]">Cho, J. H. & Hariharan, B. (2019). On the efficacy of knowledge distillation. In: ICCV.</a>

[4] <a name="[4]">Minami, S., Hirakawa, T., Yamashita, T. & Fujiyoshi, H. (2019). Knowledge transfer graph for deep collaborative learning. arXiv preprint arXiv:1909.04286.</a>

