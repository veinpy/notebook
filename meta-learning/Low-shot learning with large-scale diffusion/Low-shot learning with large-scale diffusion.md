

# Low-shot learning with large-scale diffusion

by Facebook AI Research

好像有点简单

然后疑问：infer的时候好办么

## Label Propagation

+ kNN graph connecting similari datas.
+ approximate k-nearest neighbor search
+ approach1: *FAISS library*
+ approach2: W = D.inverse * (W\_0.transpose + W\_0), where W is sparse matrix, k nearest neighbors are 1 others are 0.
+ label diffusion algorithm
+ The method initializes li to a one-hot vector for
the seeds. Background images are initialized with 0 probabilities for all classes
+ L_t+1 = W * L_t
+ (**detrimental to accuracy for few-shot learning**)can optionally reset the L rows corresponding to
seeds to their 1-hot ground-truth at each iteration
+ add priorities
+ normalization operation for L_t+1
+ *Multiclass assumption* (like l1 norm for rows of L, normalize while leaving all-0 unchanged)
+ class frequency priors. (like l1 norm for columns of L)

## related model

**Markov Clustering (MCL)**