# Busqueda binaria de un elemento en una matriz
import random, math

def binarySearchMatrix(matriz, target):
  #Dada una matriz de enteros ordenados (de menor a mayor, de izquierda a derecha y de arriba hacia abajo) y un número entero, devuelve "Verdadero" si este número se encuentra en la matiz, caso contrario devuelve Falso
  numFilas = len(matriz)
  numColumnas = 0
  if numFilas > 0:
    numColumnas = len(matriz[0])
  p_inicial = {"fila": 0, "columna": 0};
  p_final = {"fila": numFilas - 1, "columna": numColumnas - 1}
  while(p_inicial["fila"] < p_final["fila"]):
    fila_medio = math.floor((p_inicial["fila"] + p_final["fila"]) / 2)
    if matriz[fila_medio][numColumnas - 1] == target:
      return True
    elif matriz[fila_medio][numColumnas - 1] < target:
      p_inicial["fila"] = fila_medio + 1
    else:
      p_final["fila"] = fila_medio
      
  while(p_inicial["fila"] == p_final["fila"] and p_inicial["columna"] <= p_final["columna"]):
    columna_medio = math.floor((p_inicial["columna"] + p_final["columna"]) / 2)
    if matriz[p_inicial["fila"]][columna_medio] == target:
      return True
    elif matriz[p_inicial["fila"]][columna_medio] < target:
      p_inicial["columna"] = columna_medio + 1
    else:
      p_final["columna"] = columna_medio - 1
  return False

def generateMatriz(numFilas, numColumnas):
  # Dada una cantidad de filas y columnas mayores que 0, devuelve una matriz de enteros (con valores de entre -100 y 100) ordenados (de menor a mayor, de izquierda a derecha y de arriba hacia abajo)
  matriz = []
  array = []
  for i in range(numFilas * numColumnas):
    array.append(random.randint(-100, 100))
  array.sort()
  for i in range(numFilas):
    matriz.append(array[i * numColumnas : (i + 1) * numColumnas])
  return matriz

def main():
  matriz = generateMatriz(10,10)
  print(matriz)
  isFound = binarySearchMatrix(matriz, 0)
  print(isFound)
  
main()