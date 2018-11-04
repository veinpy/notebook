# Variational Lossy Autoencoder

[OpenReview](https://openreview.net/forum?id=BysvGP5ee)

---

### Introduction

apply VAE to sequence modeling.  
  
in most cases when an RNN autoregressive decoding distribution is used, the latent code **z** is completely ignored and the model regresses to be a standard unconditional RNN autoregressive distribution that doesn;t depend on teh latent code.  
because early in the training the approximate posterior **q(z|x)** carries little information about datapoint **x** and hence it's easy for the model to just set the approximate posterior to be the prior to avoid paying any regularization cost D\_KL(q(z|x) || p(z)). Even if we can solve optimizatin problems exactly, the latent code should still be ignored at optimum for most practical instances of VAE that have intractable true posterior distributions and sufficiently powerful decoders.


---
###  Bits-Back Coding