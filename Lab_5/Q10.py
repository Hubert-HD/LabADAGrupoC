# Q10: What is the time complexity of
import random

n = int(random.random() * 100)
for i in range(n):
  pass

for j in range(n):
  pass
""""
  for i in range(n):        O(n)
    pass

  for j in range(n):        O(n)
    pass

  O(n) + O(n) = O(2n)
  O(2n) ~= O(n) 
  O(n)
"""