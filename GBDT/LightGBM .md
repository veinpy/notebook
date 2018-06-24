### LightGBM 
use a novel technique of Gradient-based One-Side Sampling (GOSS) to filter out the data instances for finding a split value 

```text
Grandient-based sampling:
	Gradient represents the slope of the tangent of the loss function, 
	so logically if gradient of data points are large in some sense, 
	these points are important for finding the optimal split point as they have higher error.
	
GOSS keeps all the instances with large gradients and performs random 
sampling on the instances with small gradients.
In order to achieve a good balance between reducing the number of data 
instances and keeping the accuracy, GOSS introduces a constant multiplier
for the data instances with small gradients for keeping the same data 
distribution, when computing the [information gain]
```

### XGBoost
use pre-sorted algorithm & Histogram-based algorithm for computing the best split.

```text
pre-sorting splitting work:
	For each node, enumerate over all features
	For each feature, sort the instances by feature value
	Use a linear scan to decide the best split along that feature basis [information gain]
	Take the best split solution along all the features
```