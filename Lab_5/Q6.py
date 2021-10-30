# Q6: What is the time complexity of
import random

n = int(random.random() * 100)
i, p = 0, 0
while p <= n:
  p = p + i
  i = i + 1

""""
  valor de i     valor de p

      1             1
      2             1 + 2
      3             1 + 2 + 3
      4             1 + 2 + 3 + 4
      .             .
      .             .
      .             .
      k             1 + 2 + 3 + ... + k

    p > n
    1 + 2 + 3 + ... + k > n

    k(k-1)/2 >= n
    k^2 ~ n
    k ~ n^(1/2)
    
    O(n^(1/2))
"""