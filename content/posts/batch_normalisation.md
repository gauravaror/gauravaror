---
title: "Batch Normalisation"
date: 2020-04-15T19:41:54+10:00
draft: true
---
We take a deeper dive into how batch normalisation works and benefits it provides during training with hands-on approach. We want to see benefits acquired in training speed by using batch normalisation and regularisation.


Machine Learning Training Bottlenecks:
1. notoriously hard to train models with saturating nonlinearities
2. slows down the training by requiring lower learning rates 
3. careful parameter initialization

Benefits:

1. Making normalisation part of model architecture and as part of each minibatch (hence name Batch Normalisation).
2. Act as a regulariser eliminating the need for dropout.
3. Achieves same accuracy fewer training steps.
4. Achieves better accuracy.
5. we could ensure that the distribution of nonlinearity inputs remains more stable as the network trains, then the optimizer would be less likely to get stuck in the saturated regime, and the training would accelerate
6. Allow network to use higher learning rate as it allows the network to not grow
7. Allow larger jacobian to have singular value closer to 1.


Motivations:
Traditional Machine learning systems are able generally do standarization of features to stabilize the training. Consider example from deeplearning.ai video. If we have two features for training a machine learning model namely age and number of kilometers driven. Since range is very diverse it's very unlikely we might have problem of gradient explosion. (This standardization is know as whitening)

1. Gradient explosion because of normalisation.
2. Sigmoid derivative as x increases goes to zero, hence gradient will vanish. Since x is affected by all the layers below hence it's more likely to go into saturated range. This will make the training extremely slow.
require us to make new

Implementation Details and why:

1. Batch normalisation is done per dimension...
2. Normalisation process needs to be inside gradient descent else the parameters will blow up.
3. per-dimension is also a requirement because we want to do it for mini-batch.
4. Added \sigma for stability.
5. Doing join requires covariance matrix but no of samples in mini-batch < number of dimension hence it's matrix is singular... this would result in us requiring regularisation.
6. derives its power from normalizing activations, and from incorporating this normalization in the network architecture itself
7. Batch Norm for convolution is slighly different is per feature map instead of per activation ?????
8. Batch norm paper describes the batch normalisation is applied after affine transformation and it makes the distribution stable..... transformer doesn't use batch norm after activation rather it used the batch norm after the self attention module and end after all affine transformation and second feedforward layer doesn't even do activations :-o

Reference:

[1] Original Batch Norm paper: https://arxiv.org/pdf/1502.03167.pdf
[2] https://gab41.lab41.org/batch-normalization-what-the-hey-d480039a9e3b
[3] https://chrisyeh96.github.io/2017/08/28/deriving-batchnorm-backprop.html
[4] http://cthorey.github.io./backpropagation/
[5] https://kratzert.github.io/2016/02/12/understanding-the-gradient-flow-through-the-batch-normalization-layer.html
[6] https://towardsdatascience.com/batch-normalization-in-neural-networks-1ac91516821c 
