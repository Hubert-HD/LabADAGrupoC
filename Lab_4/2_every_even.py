# every_even implementado en python
# Complejidad: O(n2) cuadrática

def every_even(array):
  for i in range(len(array)):
    if i % 2 == 0:
      for j in array:
        print(array[i] + j)

array = [1,2,3]
every_even(array)

