""" Breadth First Search """

NO_VISITADO = -1
def breadthFirstSearch(matriz, source):
  """ Devuelve en la menor cantidad de pasos que se debe avanzar desde el punto "source"
      para llegar a cualquier casilla del "matriz", para ello se aplica la búsqueda en anchura """
  numStep = 0
  x = source["x"]
  y = source["y"]
  queue = []
  queue.append({"x": x, "y": y})
  matriz[x][y] = 0
  while len(queue) > 0:
    element = queue.pop(0)
    x = element["x"]
    y = element["y"]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx != -1 and ny != -1 and nx != len(matriz) and ny != len(matriz[0]) and matriz[nx][ny] == NO_VISITADO:
        matriz[nx][ny] = matriz[x][y] + 1
        if numStep < matriz[nx][ny]:
          numStep = matriz[nx][ny]
        queue.append({"x": nx, "y": ny})
  return numStep

matriz = [
  [-1,-1,-1,-1,-1],
  [-1,-1, 0,-1,-1],
  [-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1],
  [-1,-1,-1,-1,-1]
]
for i in range(len(matriz)):
  print(matriz[i])

numStep = breadthFirstSearch(matriz, {"x": 1, "y": 2})

for i in range(len(matriz)):
  print(matriz[i])

print("Min step: ",numStep)
