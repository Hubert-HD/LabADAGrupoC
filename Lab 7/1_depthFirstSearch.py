""" Depth First Search """

MURO = "#"
VISITADO = "V"
def depthFirstSearch(matriz, source):
  """ Cambia todos las casillas distintas de # y que no hayan sido visitadas, por una V,
      aplicacndo la búsqueda en profundidad """
  x = source["x"]
  y = source["y"]
  matriz[x][y] = VISITADO
  dx = [0, 1, 0, -1]
  dy = [-1, 0, 1, 0]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx != -1 and ny != -1 and nx != len(matriz) and ny != len(matriz[0]) and matriz[nx][ny] != MURO and matriz[nx][ny] != VISITADO:
      depthFirstSearch(matriz, {"x": nx, "y": ny})

matriz = [
  ['#','#','#','#','#','#'],
  ['#','0','0','0','0','#'],
  ['#','0','0','0','0','#'],
  ['#','0','0','0','0','#'],
  ['#','0','0','0','#','0'],
  ['#','#','#','#','0','0']
]

depthFirstSearch(matriz, {"x": 2, "y": 2})
for i in range(len(matriz)):
  print(matriz[i])

print("\n")

depthFirstSearch(matriz, {"x": 4, "y": 5})
for i in range(len(matriz)):
  print(matriz[i])