""" Ejercicio 3 """

def minNumArrayRotate(array):
  """ Devuelve el menor número del array, si es un array vacio devuelve None """
  minNum = None
  left = 0
  right = len(array) - 1
  if right == left:
    return array[0]
  while left < right:
    mid = int(left + (right - left) / 2)
    if right - left == 1:
      if array[left] > array[right]:
        return array[right]
      else:
        return array[left]
    elif array[mid] <= array[right]:
      right = mid
    else:
      left = mid
  return minNum

res = minNumArrayRotate([])
print(res)
res = minNumArrayRotate([155])
print(res)
res = minNumArrayRotate([5, 8, 11, 15, -81, -24, -1])
print(res)
res = minNumArrayRotate([11, 8, 8, 8, 7, 9, 10])
print(res)
res = minNumArrayRotate([5, 8, 11, 15, 81, 94, 100])
print(res)