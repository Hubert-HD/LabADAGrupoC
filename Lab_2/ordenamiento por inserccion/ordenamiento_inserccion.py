# Implementar el algoritmo de ordenamiento por inserccion
import random, time, json

def insertionSort(array):
  # Ordena los elementos de un arreglo de enteros ascendentemente
  for j in range(1,len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] > key:
      array[i + 1] = array[i]
      i = i - 1
    array[i + 1] = key

def insertionSortDescendente(array):
  # Ordena los elementos de un arreglo de enteros descendentemente
  for j in range(1,len(array)):
    key = array[j]
    i = j - 1
    while i >= 0 and array[i] < key:
      array[i + 1] = array[i]
      i = i - 1
    array[i + 1] = key

def generateArray(size):
  # Dada un tmaño mayor que 0, devuelve una arreglo de enteros (con valores de entre -1000000 y 1000000)
  array = []
  for i in range(size):
    array.append(random.randint(-1000000, 1000000))
  return array

def main():
  # Guarda en un archivo json los tiempos de ejecucion del algoritmo de ordenamiento por inserccion para determidadas entradas
  data = [["#Datos", "Tiempo de ejecucion"],]
  for i in [0,10,100,1000,2500,5000,7500,10000]:
    array = generateArray(i)
    tic = time.perf_counter()
    check = insertionSort(array)
    toc = time.perf_counter()
    #print(f"{i} Tiempo transcurrido {toc - tic:0.6f}")
    data.append([i, toc - tic])
  with open('ordenamiento_inserccion.json', 'w') as file:
    json.dump(data, file)

main()