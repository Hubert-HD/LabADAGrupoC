""" Máxima área de una isla """

AGUA = 0
TIERRA = 1
VISITADO = 2

def maxIslandArea(matriz):
  """ Encuentra área máxima de una isla en la matriz 2D y lo retorna """
  maxSize = 0
  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if matriz[i][j] != AGUA and matriz[i][j] != VISITADO:
        size = explorar(matriz, {"x": i, "y": j})
        if size > maxSize:
          maxSize = size
  return maxSize

def explorar(matriz, origin):
  """ Marca una zona de tierra como visitada y retona su área """
  size = 1
  x = origin["x"]
  y = origin["y"]
  matriz[x][y] = VISITADO
  dx = [0, 1, 0, -1]
  dy = [-1, 0, 1, 0]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx != -1 and ny != -1 and nx != len(matriz) and ny != len(matriz[0]) and matriz[nx][ny] != AGUA and matriz[nx][ny] != VISITADO:
      size = size + explorar(matriz, {"x": nx, "y": ny})
  return size

matriz = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

maxArea = maxIslandArea(matriz)
print(maxArea)