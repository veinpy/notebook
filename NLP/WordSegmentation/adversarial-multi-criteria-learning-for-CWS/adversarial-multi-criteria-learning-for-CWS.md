# adversarial-multi-criteria-learning-for-CWS

[github](https://github.com/FudanNLP/adversarial-multi-criteria-learning-for-CWS)

```
heterogeneous corpora can help each other

we regard each segmentation criterion
as a single task and propose three different
shared-private models under the framework
of multi-task learning, where a shared layer
is used to extract the criteria-invariant features,
and a private layer is used to extract the criteriaspecific
features. 

```

General architecture of neural CWS (chinese word segment):

+ a character embedding layer
+ **feature layers (feature extraction)** consisting of several classical neural networks
+ tag inference layer  (tags always be {B,M,E,S})
	+ CRF layer

--
### Adversarial 
**domain adaptation**

additionally introduce an **advarsarial loss** 

+ use a **criterion discriminator** which aims to recognize which criterion the sentence is annotated by using the shared features.