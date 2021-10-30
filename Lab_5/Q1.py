# Q1: What is the time complexity of
import random

n = int(random.random() * 100)
for i in range(n):
  pass

""""
  iteracion     value de i

      1             0
      2             1
      3             2
      .             .
      .             .
      .             .
      k             k-1

    i >= n
    k-1 >= n
    k ~ n
    
    O(n)
"""
