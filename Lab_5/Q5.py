# Q5: What is the time complexity of
import random

n = int(random.random() * 100)
for i in range(n):
  for j in range(i):
    pass

""""
for i in range(n):        (i*1)*n
  for j in range(i):      i
    pass                  1

  (i*1)*n = i*n 
  i ~= n
  n*n = O(n^2)
"""
