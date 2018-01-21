### Sharp vs. Flat Minima

* Flatness of minima is hypothesized to have something to do with generalization in deep nets.
* Flatness is sensitive to reparametrization and thus cannot predict geneeralization ability alone. [Dinh et al 2017](https://arxiv.org/abs/1703.04933)
* [Li et al 2017](https://openreview.net/forum?id=HkmaTz-0W) use a form of parameter normalization to make their method more robust to reparametrization and produce some fancy plots comparing deep net architectures. 
* While this analysis is now invariant to the particular type of reparametrizations considered by Dinh et al, <mark>it may still be sensitive to other types of invariances</mark>, so I'm not sure how much to trust these plots and conclusions. 
*

Interestingly, **stochastic gradient descend(SGD) with small batchsizes appears to locate minima with better generazlization properties than large-batch SGD.**

As Dinh et al (2017) pointed out, flatness is sensitive to reparametrizations of the neural network: we can reparametrize a neural network without changing its outputs while making sharp minima look arbitrarily flat and vice versa. As a consequence the **flatness alone cannot explain or predict good generalization.**

Li et al (2017) proposed a normalization scheme which scales the space around a minimum in such a way that the apparent flatness in 1D and 2D plots is kind of invariant to the type of reparametrization Dinh et al used. The proposed method (the reviewer thought) is **weakly motivated and only addresses one possible type of reparametrization.**