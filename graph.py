class Graph:

  def __init__(self, n):
    self.graph = [[Cell(i, j, '-') for i in range(n)] for j in range(n)]
    self.length = n

  # Insert value to target location
  def insert(self, r, c, value):
    self.graph[r][c] = Cell(r, c, value)

  # Print out the graph
  def draw(self):
    for row in self.graph:
      for cell in row:
        print(cell.value, end="")
      print("")

  # Return target cell
  def get_cell(self, r, c):
    if 0 <= r <= self.length-1 and 0 <= c <= self.length-1:
      return self.graph[r][c]
    else:
      return None

  # Return valid neighbors from any cell on graph
  def get_neighbors(self, c):
    candidates = list(filter(None, [self.get_cell(c.r - 1, c.c), self.get_cell(c.r + 1, c.c),
                                    self.get_cell(c.r, c.c - 1), self.get_cell(c.r, c.c + 1)]))

    return [c for c in candidates if c.value != 'x']

  # Return Mario cell from graph
  def get_mario(self):
    for row in self.graph:
      for cell in row:
        if cell.value == 'm':
          return cell


class Cell:
  # Initialize rows, column and value of each cell
  def __init__(self, r, c, value):
    self.r = r
    self.c = c
    self.value = value

  def set(self, r, c):
    self.r = r
    self.c = c


