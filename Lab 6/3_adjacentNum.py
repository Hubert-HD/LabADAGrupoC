""" Ejercicio 2 """

def adjacentNum(array, target):
  """ Devuelve el número mayor o igual más proximo al "target" en array, sino existe alguno devuelve None """
  adjacent = None 
  left = 0
  right = len(array) - 1
  while left <= right:
    mid = int(left + (right - left) / 2)
    if array[mid] == target:
      return array[mid]
    if array[mid] > target:
      adjacent = array[mid]
      right = mid - 1
    else:
      left = mid + 1
  return adjacent

array = [-81, -24, -1, 0, 2, 5, 5, 11, 15]
res = adjacentNum(array, -500)
print(res)
res = adjacentNum(array, 6)
print(res)