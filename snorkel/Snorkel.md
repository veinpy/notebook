# Snorkel

Rather than viewing training data as a perfectly correct input provided a priori, we view the labeling of training data as a stochastic process that we can model. Surprisingly, by learning this model, we can use potentially low-accuracy labeling functions to train high-accuracy end models.

model labeling functions as a generative process, which let us automatically denoise the resulting training set by learning the accuracie of the lableing functions along with their correlation structure.

labeling functions can be based on external knowledge bases, libraries or ontologies, can express heuristic patterns, or some hybrid of these types.

---

#### Standard Pipeline Shortage
normal machine learning bottleneck
> hand-labeled training data is not available or expensive
> related external knowledgre bases are unavailable or insufficiently specific
> application specifications are in flux

---

### Data Programming
[paper](https://arxiv.org/abs/1605.07723)

**labeling function**
> labeling subset of available data, which may have arbitrary unknown accuracies, and may overlap and conflict with each other.
(1) modeling outputs of the labeling functions with a <mark>generative model</mark>
(2) training an end model with the estimated labels.

> Given enough labeling functions of high enough average quality, the end performance of the model we are ultimately training scales with respect to the amount of unlabeled data used at the same asymptotic rate as in the fully supervised case.


##### Each Labeling Function is iid.
> each labeling function λi has some probability βi of labeling an object and then some probability αi of labeling the object correctly.
> 
> Use Maximum likelihhod estimation to learnn the λi and βi.

---

##### Dependence of Labeling Function

---

##### Noise-Aware Empirical Loss
 
