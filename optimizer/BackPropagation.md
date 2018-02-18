# BackPropagation

**[Chinese blog illustration](https://www.evernote.com/shard/s659/sh/17c00f63-4573-4def-bf36-8f040f010e42/3bb2844057352e4513491764fb412160)**

[slides from Sebastian](resources/optimizationtalk-171126132036.pdf)

### optimizer to choose
> Adaptive learning rate methods (Adagrad, Adadelta, RMSprop, Adam) are **particularly useful for sparse features**.

> Adagrad, Adadelta, RMSprop, andAdam work well in similar circumstances.
> 
> [Kingma and Ba 2015] show that bias-correction helps Adam **slightly outperfom RMSprop**.
> 
> SGD with tuned learning rate and momentum is **competitive with Adam**. [Zhang 2017]
> 
> Adam **converges faster**, but **underperforms SGD** on some tasks, e.g. Machine Translation [Wu 2016]
> 
> Adam with **2 restarts and SGD-style annealing** converges faster and outperforms SGD [Denkowskiand Neubig 2017]
> 
> **Increasing the batch size** may have the same effect as decaying the learning rate [Smith 2017]

### Additional Strategies for optimizing SGD

> Shuffling and Curriculum Learning [Bengio 2009]

> 		Shuffle training data after every epoch to **break biases**
>		Order training examples to **solve progressively harder problems**: infrequently used in practice 
>
> Batch normalization [loffe and Szegedy, 2015]
> 	
> 		**Re-normalizes every mini-batch** to zero mean, unit variance
> 
> Early Stopping
> 
> 		"Early stopping (is) beautiful free lunch" (Geoff Hinton)
> 
> Gradient noise [Neelakantan 2015]
> 		
> 		Add Gaussian noise to gradient
>	 	Makes model **more robust to poor initliazations**
> 
> **cosine annealing schedule**.
> 
> **Snapshot ensembles** 
> 		
> 		[SGD vs. snapshot ensembles 2017]
> 
> 		Train model until convergence with cosine annealing schedule.
> 		Save model parameters
> 		Perform warm restart and repeat steps 1-3 M times.
> 		Ensemble saved models.
> 
> Learning to optimize
> 		
> 		Neural Optimizer Search [Bello 2017]