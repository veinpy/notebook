## read list


### Generative Paper
[Improved Variational Inference with Inverse Autoregressive Flow](https://arxiv.org/pdf/1606.04934v2.pdf), [github](https://github.com/openai/iaf)

<mark>http://bjlkeng.github.io/posts/variational-autoencoders-with-inverse-autoregressive-flows/

https://blog.evjang.com/2018/01/nf2.html


```	
allow your variational autoencoder to fit better by concentrating the samples stochastic around a closer approximation to the true posterior

for latent datas *z*, if *z* has many dimensions, then to properly cover the space you'll need an exponential number of examples roughly (10)**n_dim datasets, eliminating the facts that some samples are very low probable in the latent space, contributing nothing to your network weights.

fully factorized diagnoal Gaussian distributions 是VAE的一个强假设，这妨碍了它对更加复杂的posterior distribution 的拟合

Normalizing Flow (1-map-1 transformation) 用invertible transormation 将distribution映射到更复杂的distribution，来拟合posterior distribution
```

### Module

[Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf).    ·[{blog}](https://blog.openai.com/language-unsupervised/#content)

```
	by openai
```

[Meta-Learning by the Baldwin Effect](https://arxiv.org/pdf/1806.07917.pdf)

	by google
	shaping hyperparamaters and the initial parameters of dl algorithms
	MAML (Model Agnostic Meta-Learning)

[META-LEARNING WITH LATENT EMBEDDING OPTIMIZATION](https://arxiv.org/pdf/1807.05960v2.pdf)

	by google
	learning a data-dependent latent generative representatoin of model parameters
	latent embedding optimization(LEO)
	

### Chatbot

[MACHINE LEARNING FOR DIALOG STATE TRACKING: A REVIEW](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/44018.pdf)
```
	by google
```