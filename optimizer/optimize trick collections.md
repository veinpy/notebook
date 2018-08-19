To **avoid overfitting**, we apply an 1×1 convolution on the attention weighted feature map to reduce the number of channels, resulting in a reduced feature map Ir. 



g(.) is the element-wise scaled hyperbolic tangent function: g(x) =1.7159 · tanh( 23x) [【13】](Efficient backprop In Neural networks: Tricks of the trade).  This function leads the gradients into the most non-linear range of value and enables a higher training speed.