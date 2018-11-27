# Meta Learning Summary

+ compositionality
+ causality
+ learning to learn

## mainly methods
+ recurrent models
+ metric learning
+ learning optimizers

--
1. information must be stored in memory in a representation that is both stable and element-wise addressable
2. the number of parameters should not be tied to the size of the memory 

--
### recurrent models

[instance paper](http://proceedings.mlr.press/v48/santoro16.pdf)

LSTM based model

--
### metric learning

scoring the new sample, by comparing it with the sample we already have.

reference: 
[matching network](../Matching Networks for One Shot Learning/Matching Networks for One Shot Learning.md) 
[relation network](../Learning to Compare: Relation Network for Few-Shot Learning/Learning to Compare: Relation Network for Few-Shot Learning.md)

--
### Learning Optimizer

two optimizations at play: 

1. the learner, which learns new tasks
2. meta-learner, trains the learner

[instance paper](https://openreview.net/forum?id=rJY0-Kcll)