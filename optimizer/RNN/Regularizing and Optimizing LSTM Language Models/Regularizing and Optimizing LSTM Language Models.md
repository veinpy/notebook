# Regularizing and Optimizing LSTM Language Models

[【ICLR2018 OPENREVIEW】](https://openreview.net/forum?id=SyyGPP0TZ)

---

+ weight-dropped LSTM which uses **DropConnect** on hidden-to-hidden weights as a form of recurrent regularization.
+ randomized-length backpropagation through time (BPTT), embedding dropout, activation regularization (AR), and temporal activation regularization (TAR)  
+ NT-ASGD, a variant of the averaged stochastic gradient method, wherein the averaging trigger is determined using a non-monotonic condition as opposed to being tuned by the user
