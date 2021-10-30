# Q3: What is the time complexity of
import random

n = int(random.random() * 100)
for i in range(0, n, 2):
  pass

""""
N° iteracion     value de i

      1             0
      2             2
      3             4
      .             .
      .             .
      .             .
      k           2(k-1)

    i >= n
    2(k-1) >= 0

    2(k-1) >= n
    k ~ n

    O(n)
"""
