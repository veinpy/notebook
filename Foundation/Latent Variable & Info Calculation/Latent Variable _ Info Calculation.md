# Latent Variable & Info Calculation


### Lantent Variables   
```Info Compression | Reduction```  


+ Dimensionality reduction works only if the inputs are correlated (images in same domain). So we needs the network auto-classify the categorys


### Missing examples even the generative model (like autoencoder)   

```text
For autoencoder, 

The ENCODER produce encoded data which could present the info from input; the DECODER reconstruct the input via the encoded data. 

After training phase, if we use the DECODER produce the data by feeding in manually encoded data which may not seen in the training phase, the produced data have a chance be very blur. 

Like the img below```  

<img src="blur image and clear images.png" alt="blur image and clear images" width="250"/>

**Essentially, the generative model is still a discriminative model with constructing the complete info to generate the ideal data**  

#### reparametrization trick  
the encoder produce the complete info for the prior distribution. Then produce the latent variable by sampling the encoded latent variable's distribution. Ideally, the sampling process could cover all the situations.   
But *maybe less efficient*.


**Latent Variables Reasoning**


---
### Reference
[A wizard’s guide to Adversarial Autoencoders](https://towardsdatascience.com/a-wizards-guide-to-adversarial-autoencoders-part-1-autoencoder-d9a5f8795af4)