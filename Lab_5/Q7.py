# Q7: What is the time complexity of
import random

n = int(random.random() * 100)
i = 1
while i < n:
  print(i)
  i = i * 2

""""
  N° iteracion     value de i

      1             1
      2             1 * 2
      3             (1 * 2) * 2
      4             ((1 * 2) * 2) * 2
      .             .
      .             .
      .             .
      k             1 * 2^(k-1)

    i > n
    2^(k-1) > n
    
    2^k ~ n
    k ~ log2(n)
    
    O(log(n))
"""