# Q2: What is the time complexity of
import random

n = int(random.random() * 100)
for i in range(n,0,-1):
  pass

""""
N° iteracion     value de i

      1             n
      2             n-1
      3             n-2
      .             .
      .             .
      .             .
      k             n-(k-1)

    i <= 0
    n-(k-1) <= 0

    (k-1) >= n
    k ~ n

    O(n)
"""
