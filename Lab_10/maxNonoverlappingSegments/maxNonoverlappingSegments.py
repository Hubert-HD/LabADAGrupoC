# Ejercicio 1
# https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/

def solution(A, B):
  if len(A) < 2:      
    return len(A)
  count = 1
  end = B[0]
  i = 1
  while i < len(A):
    while i < len(A) and A[i] <= end:
      i += 1
    if i == len(A):
      break
    count += 1
    end = B[i]
  return count