# Snorkel

Rather than viewing training data as a perfectly correct input provided a priori, we view the labeling of training data as a stochastic process that we can model. Surprisingly, by learning this model, we can use potentially low-accuracy labeling functions to train high-accuracy end models.

---

### Data Programming
[paper](https://arxiv.org/abs/1605.07723)

**labeling function**
> labeling subset of available data, which may have arbitrary unknown accuracies, and may overlap and conflict with each other.
(1) modeling outputs of the labeling functions with a <mark>generative model</mark>
(2) training an end model with the estimated labels.

>> Given enough labeling functions of high enough average quality, the end performance of the model we are ultimately training scales with respect to the amount of unlabeled data used at the same asymptotic rate as in the fully supervised case.