# Implementar el algoritmo de búsqueda binaria
import random, time, json, math

def binarySearch(array, target):
  # Devuelve "Verdadero" si un número dado se encuentra en un arreglo de enteros, caso contrario devuelve "Falso"
  izquierda = 0;
  derecha = len(array) - 1
  while(izquierda <= derecha):
    medio = math.floor((izquierda + derecha) / 2)
    if array[medio] == target:
      return True
    elif array[medio] < target:
      izquierda = medio + 1
    else:
      derecha = medio - 1
  return False

def generateArray(size):
  # Dada un tmaño mayor que 0, devuelve una arreglo de enteros (con valores de entre -1000000 y 1000000)
  array = []
  for i in range(size):
    array.append(random.randint(-1000000, 1000000))
  return array

def main():
  # Guarda en un archivo json los tiempos de ejecucion del algoritmo de busqueda binaria para determidadas entradas
  data = [["#Datos", "Tiempo de ejecucion"],]
  for i in [0,10,100,1000,10000,100000,1000000]:
    array = generateArray(i)
    array.sort()
    tic = time.perf_counter()
    check = binarySearch(array, 0)
    toc = time.perf_counter()
    data.append([i, toc - tic])
  with open('busqueda_binaria.json', 'w') as file:
    json.dump(data, file)

main()