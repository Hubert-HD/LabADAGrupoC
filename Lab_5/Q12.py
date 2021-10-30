# Q12: What is the time complexity of
import random

n = int(random.random() * 100)

for i in range(n):
  j = 1
  while j < n:
    j = j * 2

""""
  for i in range(n):        n * O(log(n))
    j = 1                   
    while j < n:            O(log(n))
      j = j * 2             

  O(n * O(log(n))) ~= O(nlog(n))
"""