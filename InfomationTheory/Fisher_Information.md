# Fisher

## Fisher Infomation Matrix

(函数latex表达式)：    
\mathcal{I}\left(\boldsymbol{\theta}^{*}\right)_{i, j}=\mathbb{E}_{\boldsymbol{\theta}^{*}}\left[\left(\left.\frac{\partial}{\partial \theta_{i}} \log p(Y \mid \boldsymbol{\theta})\right|_{\boldsymbol{\theta}=\boldsymbol{\theta}^{*}}\right)\left(\left.\frac{\partial}{\partial \theta_{j}} \log p(Y \mid \boldsymbol{\theta})\right|_{\boldsymbol{\theta}=\boldsymbol{\theta}^{*}}\right)\right]

```fisher information matrix is the covariance matrix of the log likelihood gradient with respect to the parameters when we evaluate that gradient at the true parameter vector and the randomness comes from that true paramter vector```

---------------------- 

\mathcal{I}\left(\boldsymbol{\theta}^{*}\right)_{i, j}=-\mathbb{E}_{\boldsymbol{\theta}^{*}}\left[\left.\frac{\partial^{2}}{\partial \theta_{i} \partial \theta_{j}} \log p(Y \mid \boldsymbol{\theta})\right|_{\theta=\boldsymbol{\theta}^{*}}\right]


```as in hessian view, an element of the fisher infomation matrix also turns out to be equal to the negative expected of the second partial derivative for the two parameters associated with that element```

## Reference
[https://www.youtube.com/channel/UCCcrR0XBH0aWbdffktUBEdw](https://www.youtube.com/channel/UCCcrR0XBH0aWbdffktUBEdw)
