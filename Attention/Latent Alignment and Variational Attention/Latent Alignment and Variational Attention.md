# Latent Alignment and Variational Attention

[paper](https://arxiv.org/abs/1807.03756)
[github](https://github.com/harvardnlp/var-attn)

--
### key idea:
<mark>**evidence lower bound optimization(ELBO)**

inference network takes in the input, query, and the output, produce parameters of the variational distribution q(z; λ). i.e. λ = enc(x, x_~, y; φ).

--
## Shortage

+ 1. Variational/hard attention needs a good baseline estimator in the form of soft attention. (necessary component for adequately training)
+ For some applications, the model relies heavily on having a good posterior estimator. (utilize domain structure for **enc** function)
+ Recent models such as the Transformer, utilize many repeated attention models. It is unclear if this approach can be used at that scale.