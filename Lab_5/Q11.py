# Q11: What is the time complexity of
import random

n = int(random.random() * 100)
p = 0
i, j = 1, 1

while i < n:
  p = p + 1
  i = i * 2

while j < p:
  j = j * 2

""""
  p = 0
  i, j = 1, 1

  while i < n:        O(log2(n))
    p = p + 1
    i = i * 2
  
  while j < p:        O(log2(p))
    j = j * 2

  O(log2(n)) + O(log2(p)) = O(log2(n) + log2(p))
  O(log2(n) + log2(p))
  O(log2(n*p))

  p ~= log2(n)
  O(log2(n*log2(n)))
  log2(n) ~= n
  O(log2(n^2))
  O(2*log2(n))

  O(log(n))
"""