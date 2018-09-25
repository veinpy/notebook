#### Activation
Selection of the activation function is mostly dependent on the problem and nature of the data. For example, ** "sigmoid" **is suitable for networks where the output is in the range \[0,1\], however, the ** "tanh" ** and ** "sigmoid" ** activation functions saturate the neuron very fast and can vanish the gradient.  Despite ** "tanh", the non-zero centered output from "sigmoid" can cause unstable dynamic in the gradient updates for the weights.**  The ** "ReLU" ** actiation function leads to sparser gradients and greatly accelerates the convergence of stochastic gradient descent (SGD) compared to the "sigmoid" or "tanh" activation functions. 

#### Loss Function

Euclidean distance and Hamming distance for forecasting of real-values and cross-entropy over probability distribution of outputs for classification problems.

