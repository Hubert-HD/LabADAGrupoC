# Implementar la busqueda secuencial
import random, time, json

def secuentialSearch(array, target):
  # Devuelve "Verdadero" si un número dado se encuentra en un arreglo de enteros, caso contrario devuelve "Falso"
  for i in range(len(array)):
    if array[i] == target:
      return True
  return False

def generateArray(size):
  # Dada un tamaño mayor que 0, devuelve una arreglo de enteros (con valores de entre -1000000 y 1000000)
  array = []
  for i in range(size):
    array.append(random.randint(-1000000, 1000000))
  return array

def main():
  # Guarda en un archivo json los tiempos de ejecucion del algoritmo de busqueda secuencial para determidadas entradas
  data = [["#Datos", "Tiempo de ejecucion"],]
  for i in [0,10,100,1000,10000,100000,1000000]:
    array = generateArray(i)
    tic = time.perf_counter()
    check = secuentialSearch(array, 0)
    toc = time.perf_counter()
    #print(f"{i} Tiempo transcurrido {toc - tic:0.6f}")
    data.append([i, toc - tic])
  with open('busqueda_secuencial.json', 'w') as file:
    json.dump(data, file)
    
main()