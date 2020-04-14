---
title: "Converting Transformer Encoder into classifier"
date: 2020-02-20T16:47:14+11:00
draft: true
---

The architectures based on transformers enabled successful transfer learning in NLP tasks. The architectures based on RNN's required hacks such as Gradual unfreezing, slanted traingular learning rate to enable pre-training be useful for down stream tasks. This distinction made us wonder if transformers have innate ability to reduce forgetting. The transformers are sequence to sequence encoder, we need to convert the sequence to sequence representation into a single vector which can be used for classification. To convert the transformer encoded sequence into a vector we experimented with following three strategies i.e using CLS token representation, Mean of all the token sequence representation, Max representation. After experimentation we decided to pick the mean representation.

Use representation of CLS token
================================

The  BERT appended the tokens with CLS token and used the special token representation for classification. When using the CLS token technique when transformers are trained on medium size task, architecture is not able to learn a good representation even for a single task. Training TREC acheives accuracy of 90\% when trained using LSTM and CNN's. Whereas using CLS technique with transformers it performs slightly better than using random initialisations. We hypothised that CLS technique works well only when network has been pre-trained and learned a good representation.

Mean Representation
===================

When mean representation of all the tokens in the sequence is used as input to the classification layer we found network is able achieve accuracy of 70\% which is substantially less than accuracy for LSTM and CNN. We found the amount of forgetting with mean representation to be comparable to LSTM's but interestingly we found that with mean representaion we achieve very clean clusers for each task even after all the tasks have been trained.

Max Representation
===================

When we used max to merge representation for all tokens in the sequence as classifier input we found transformers worked at-par with accuracy achieved by LSTM's and CNN's. The max representation also helped also helped the transformers in reducing the forgetting for network.


