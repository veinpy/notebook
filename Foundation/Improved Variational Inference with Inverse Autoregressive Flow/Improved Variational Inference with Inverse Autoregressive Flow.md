# Improved Variational Inference with Inverse Autoregressive Flow

a new type of normalizing flow, inverse autoregressive flow(IAF) that scales well to high-dimensional latent spaces.

Author shows that it significantly improves diagonal Gaussian approximate posteriors. 

we train deep variational auto-encoders with latent variables at multiple levels of the hierarchy, where each stochastic variable is a three-dimensional tensor


+ 1. computatinally efficient to compute and differentiate its probability density q(z|x)  
+ 2. computationally efficient to sample from  
+ 3. parallel computational for *z*

