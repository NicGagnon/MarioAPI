class Graph:

  def __init__(self, n):
    self.graph = [[Cell(i, j, '-') for i in range(n)] for j in range(n)]

  def insert(self, x, y, value):
    self.graph[x][y] = Cell(x, y, value)

  def draw(self):
    for row in self.graph:
      for cell in row:
        print(cell.value, end="")
      print("")


class Cell:
  def __init__(self, x, y, value):
    self.x = x
    self.y = y
    self.value = value

