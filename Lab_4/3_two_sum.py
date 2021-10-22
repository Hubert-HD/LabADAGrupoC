# two_sum implementado en python
# Complejidad: O(n2) cuadrática

def two_sum(array):
  for i in range(len(array)):
    for j in range(len(array)):
      if(i != j and array[i] + array[j] == 10):
        return True
  return False

array = [1,2,3]
value = two_sum(array)
print(value)

array = [3,2,7,5]
value = two_sum(array)
print(value)

array = []
value = two_sum(array)
print(value)

array = [5,2]
value = two_sum(array)
print(value)