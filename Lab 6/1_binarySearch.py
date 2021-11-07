""" Binary search: implementacion en python """

def binarySearch(array, target):
  """ Devuelve la posicion del elemento "target" si se encuentra en el array, caso contrario devuelve -1 """
  left = 0
  right = len(array) - 1
  while left <= right:
    mid = int(left + (right - left) / 2)
    if array[mid] == target:
      return mid
    if array[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

array = [-81, -24, -1, 0, 2, 5, 5, 11, 15]
res = binarySearch(array, 7)
print(res)
res = binarySearch(array, 11)
print(res)