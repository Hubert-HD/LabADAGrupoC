""" Ejercicio 1 """

def isSquare(num):
  """" Devuelve verdadero si el número es un cuadrado, caso contrario devuelve falso """
  start = 1
  end = num
  while start <= end:
    mid = int(start + (end - start) / 2)
    square = mid * mid
    if square == num:
      return True
    if square > num:
      end = mid - 1
    else:
      start = mid + 1
  return False


for i in range(26):
  res = isSquare(i)
  print(i, " es ", res)