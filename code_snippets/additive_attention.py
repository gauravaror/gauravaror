import torch
import torch.nn as nn

# Size of hidden dimension of model.
hidden_dim = 128
# Size of encoder, considering encoder was bi-directional.
key_size = 2*hidden_dim
# Decoder is not birectional hence not multiplied by 2.
query_size = hidden_dim
value_size = hidden_dim
batch_size = 64
max_seq = 20


## Using the dummy key, query, values
key = torch.randn(batch_size, max_seq, key_size)
query = torch.randn(batch_size, query_size)

## Define projection layer to map key and query to same dimention
key_layer = nn.Linear(key_size, hidden_dim, bias=False)
query_layer = nn.Linear(query_size, hidden_dim, bias=False)
