# Q9: What is the time complexity of
import random

n = int(random.random() * 100)
i = 0
while i * i < n:
  print(i)
  i = i + 1

""""
  N° iteracion    value de i

      1             1
      2             4
      3             9
      4             16
      .             .
      .             .
      .             .
      k             k^k

    k^k >= n
    k ~= logk(n)
    O(log(n))
"""