---
title: "Memory networks"
date: 2019-12-11T19:41:03+11:00
draft: false
---

`Memory Networks` are neural networks which have access to explicit storage and a mechanism to access storage to answer query requiring multi-hop reasoning. 

{{< figure src="/Big_Oak.png" width="40%" align="center" >}}

<!--more-->

Memory networks are useful in solving tasks which require multiple hops of reasoning such as [Reading Comprehension with multiple hops](https://qangaroo.cs.ucl.ac.uk). The figure above shows multi-hop reasoning when relating  `Gulf Coastal Plains`  to `United States of America`

## What are memory networks?

They are neural networks which have access to long term storage and a mechanism to access part of long-term storage to answer queries. Memory networks are useful for language understanding tasks.

Let's consider we want to answer the questions based on a scenario described in multiple-lines. Below is one such scenario from dialogue-based language learning dataset in [bAbi](https://research.fb.com/downloads/babi/) dataset.

#### Story
```
SentenceId  Sentence
1.	Mary moved to the bathroom.
2	John went to the hallway.
4	Daniel went back to the hallway.
5	Sandra moved to the garden.
```

#### Questions
```
QuestionId	Question		Answer		Sentence ID
1.	Where is Mary?			bathroom	1
2. 	Where is Daniel?		hallway		4

```

We convert sentences from raw strings to memory slots, and each one will occupy one memory slot.

#### Memory slot.

A memory slot consists of a key and value pair. The network measures the similarity between the key and the query, which is used as attention to access memory content. Memory key and values are embedded using two different embedding matrices.

We can use a simple procedure to convert sentences into memory slot by using an embedding matrix. The process is similar to transforming a sentence into sentence embeddings using word vectors like word2vec or glove. We convert each token into one hot representation and then map it into a vector using embeddings. To represent a sentence, we can average the word vectors for all words in the sentence. Memory networks use two such embeddings (learned during the training) one for creating a key, other for value.

Examples of memory networks are:

### Attention over hidden states [RNNSearch](https://arxiv.org/abs/1409.0473)

Examples of memory networks are:

### Attention over hidden states [RNNSearch](https://arxiv.org/abs/1409.0473)

Seq2Seq models have an encoder and decoder modules which encoding input sequence into hidden state $h_t$, which generates output sequence. Seq2Seq models were created primarily for neural machine translation.

RNNSearch changed the way we access information from encoder hidden state $h_t$; they started using state for all words instead of just the final word. The decoder uses attention to combine and access different parts of the sentence from latent representation. All the hidden states can be considered memory and attention can be seen as a way to access different parts of memory.

Using attention to access useful parts of memory (hidden representation from RNN) can be seen as a memory network. But this type of memory only works at sentence level instead of document level and is widely used in current NLP architectures.

#### End to End Memory Networks([MemN2N](https://arxiv.org/abs/1503.08895))

The memory here is encoded representation of all the sentences in [babi](https://research.fb.com/downloads/babi/) toy story using learned embedding matrix A(`Key`) and C(`Memory Content`). While querying, the query is embedded using learned embedding matrix B(`Query`).

Memory is accessed based on the similarity between `Key` and `Query`.
$$
p_i = \mathrm{Softmax}(\mathrm{Query}^{T}.\mathrm{Key}_i)
$$

$p_i$ is used as attention over memory content `Memory Content` to access relevant part of memory to answer the query. The power of memory networks is in recursively improving the internal representation to answer the final answer based on long term memory. MemN2N generally uses multiple layers which recursively improves the representation using memory.

## What are memory networks good for?

* Can access and manipulate external long term memory.
* End to end memory networks can automatically select the memory slot to answer questions.
* Recursively improve the representation using memory.
* They are suitable for handling tasks involving dialogues due to ability to enhance the representation of current sentence/query using past chat context.

## Techniques aka Lingo used

* Linear start --
* Positional Encoding -- To encode the position of a word in the sentence.
* Content-based memory access -- Access memory based on the similarity between query and memory content. End to end memory network are capable of accessing content based memory.
* Address based memory access --  Neural Turning machine paper has address based memories aswell.
* Temporal encoding  -- To encode order of sentence in memory.
* Learning time invariance by injecting random noise --
* hops -- Multiple layers used to improve representation using long-term memory recursively.

## Practical contraints

### Explosion in parameters

Network use three different embedding matrices(`A, B, C`) for each of the hops(layers) which result in the explosion of parameters. The paper proposes the two different weight tying scheme to share the parameters in the network.

* Adjacent: The output embedding `C` is shared with input embedding `A` for the layer above this layer.
* Layer-wise: The input embedding `A` and output embedding `C` for each layer is shared.

## Major Findings

* Multiple hops help in task which requires state tracking like dialouge.
* Linear start helps in avoiding the local minima (Does that mean memory networks are more prone to get stuck in bad areas? Can pre-training help here?)
* Positional encoding works better than bag-of-word representation.
* They found improvement in language modelling task using memory networks
* These memory networks can work without the supervision of which sentence answer occurs in.

<!--### Questions:

%* Which of the weight tying mechanism is better in which scenario, cite Fie Liu paper on it.-->
