# Q4: What is the time complexity of
import random

n = int(random.random() * 100)
for i in range(n):
  for j in range(n):
    pass

""""
for i in range(n):        (n*1)*n
  for j in range(n):      n*1
    pass                  1

  (n*1)*n = O(n^2)
"""
