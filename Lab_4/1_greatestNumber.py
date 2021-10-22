# Convertir from O(n^2) to O(n)
# greatestNumber implementado en python

def greatestNumber(array):
  # Complejidad: O(n2) cuadrática
  for i in array:
    isValTheGreatest = True
    for j in array:
      if j > i:
        isValTheGreatest = False
    if isValTheGreatest:
      return i

# El array recibido debe tener al menos un elemento
def greatestNumber_modificado(array):
  # Complejidad: O(n) lienal
  mayor = array[0]
  for i in array:
    if mayor < i:
      mayor = i
  return mayor

array=[1,2,3,4,5]
print(greatestNumber_modificado(array))