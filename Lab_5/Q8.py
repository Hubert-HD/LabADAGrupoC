# Q8: What is the time complexity of
import random

n = int(random.random() * 100)
i = n
while i >= 1:
  print(i)
  i = i / 2

""""
  value de i        N° iteracion 

      1             1
      2             2
      3             2
      4             3
      .             .
      .             .
      .             .
      8             4
      .             .
      .             .
      .             .
      n             log2(n) + 1

    log2(n) + 1 ~= log2(n)
    
    O(log2(n))
    O(log(n))
"""