# Ejercicio 5
# https://open.kattis.com/problems/grass

from math import sqrt

def solution(sprinklers, length, n):
  numUsed, index, currentLength = 0, 0, 0
  while True:
    moreFar = -1
    while index < n and sprinklers[index][0] <= currentLength:
      moreFar = max(moreFar, sprinklers[index][1])
      index += 1
    if moreFar == -1:
      return -1
    numUsed += 1
    currentLength = moreFar
    if currentLength >= length:
      return numUsed

for i in range(3):
  n, length, height = map(int, input().split())
  sprinklers = []
  for i in range(n):
    position, radio = map(int, input().split())
    if (2 * radio) > height:
      distance = sqrt((radio ** 2) - ((height / 2) ** 2))
      sprinklers.append((position - distance, position + distance))
  sprinklers = sorted(sprinklers)
  numSprinklers = len(sprinklers)
  res = solution(sprinklers, length, numSprinklers)
  print(res)