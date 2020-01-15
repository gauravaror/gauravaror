import torch
import torch.nn as nn
import math


class Attention(nn.Module):
    def __init__(self, dimension: int):
        self.dim = dimension
        self.WK = nn.Linear(self.dim, self.dim)
        self.WV = nn.Linear(self.dim, self.dim)
        self.WQ = nn.Linear(self.dim, self.dim)
        self.softmax = nn.softmax(dim=2)

    def forward(self, val: torch.Tensor):
        if not val.shape()[-1] == self.dim:
            raise Exception("Dimension of input doesn't match")
        query = self.WQ(val)
        key = self.WK(val)
        value = self.WV(val)
        attention = self.softmax(query.matmul(key.transpose(-2,-1))/sqrt(math.sqrt(self.dim))).V
        return attention

class MultiHeadAttention(nn.Module):
    def __init__(self, _num_heads: int, dim: int):
        if not dim % _num_heads == 0:
            raise Exception("Dimension should be divide by number of heads in Transformer architecture")

        self.num_heads = _num_heads
        self.dim_model = dim
        self.dim_k = dim/head

        self.W_query = nn.Linear(self.dim, self.dim)
        self.W_value = nn.Linear(self.dim, self.dim)
        self.W_key = nn.Linear(self.dim, self.dim)



    def forward(self, val):
        heads_output = []

        # Find out number of batches
        n_batches = val.size(0)

        query = self.W_query(val).view(n_batches, -1, self.num_heads, self.dim_k)
        key = self.W_key(val)
        value = self.W_value(val)


        return combined_heads@self.WO
