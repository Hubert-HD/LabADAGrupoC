# Ejercicio 3
# https://open.kattis.com/problems/bank

from collections import defaultdict
from heapq import heappush
from heapq import heappop

def bankQueue(numClients, minForClose):
  clients = defaultdict(list)
  for _ in range(numClients):
    cash, time = list(int(x) for x in input().split())
    clients[time].append(cash)
  temp = []
  total = 0
  for time in range(minForClose-1, -1, -1):
    for price in clients[time]:
      heappush(temp, -price)
    if temp:
      total = total + heappop(temp)
  return (-total)

numClients, minForClose = (int(x) for x in input().split())
value = bankQueue(numClients, minForClose)
print(value)