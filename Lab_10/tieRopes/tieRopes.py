# Ejercicio 2
# https://app.codility.com/programmers/lessons/16-greedy_algorithms/tie_ropes/

def solution(K, A):
  count = 0
  length = 0
  for rope in A:
    length += rope
    if length >= K:
      count += 1; length = 0
  return count