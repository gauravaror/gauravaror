---
title: "Gradient estimation for hard non-linearities"
date: 2019-12-27T01:12:48+11:00
draft: true
---

Hard non-linearity are useful for modelling categorical variable in neural networks but cannot be trained using backpropagation algorithm as the gradient is zero almost everywhere such as step function. We review gradient estimation techniques like Gumbel softmax trick and straight through estimator to do back-prop with hard non-linearity.

<!--more-->

## Hard non-linearity

Hard non-linearities are one which has gradient almost zero everywhere such as step function. Following are two usecases for using hard activation functions:

1. Categorial Variable
> Hard non-linearities are useful in modelling choices we encounter in our everyday life. Consider a generative neural network which can generate image for digit 1 upto 10 on request. This require modelling categorial variable which to impossible to backpropogate through in the network.


2. Conditional computation or Sparse Representation
 > Usecase I am exploring is to prevent network from updating certain parts of network to prevent catastrophic forgetting of tasks learned previously. This is conditional computation task proposed By Bengio [1].

 ***

## Approaches for gradient estimation through hard non-linearities

Gradient can be estimated following four approaches compared by Bengio [1]:

### Unbiased Gradient Estimator

Bengio [1] proposed an unbiased gradient estimator for stocastic binary neurons. Stocastic binary neuron here was defined as hard non-linearity based value of a sigmoid function. Stocastic neuron is activated based on input value to sigmoid:

$$
h_i = f(a_i, z_i) = 1_{z_i > sigmoid(a_i)}
$$

They proposed a unbiased estimate of gradient and provide derviation which shows estimator they provide is unbiased and have same estimated value. They also propose a centered estimator which is shown to have minimum variance.

$$
 g_i = (h_i - sigm(a)).Loss
$$

This is interesting as you can ability to switch off part of network based on total sum of neuron and still be able to back-propogate through it. It seems they are more resiliant towards saturated units compared to ReLU activation units.

#### Decompose Binary stocastic neuron

#### Stocastic additive or multiplicative noise

### Straight through Estimator




### Questions


### References

[1] Bengio, Yoshua, Nicholas Léonard, and Aaron Courville. "Estimating or propagating gradients through stochastic neurons for conditional computation." arXiv preprint arXiv:1308.3432 (2013).
[2] Jang, Eric, Shixiang Gu, and Ben Poole. "Categorical reparameterization with gumbel-softmax." arXiv preprint arXiv:1611.01144 (2016).


