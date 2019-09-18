# Author is Nicolas Gagnon 2019
from graph import Graph, Cell
#import queue


def find_shortest_path(N, grid):
  validate_grid(N, grid)

  graph = Graph(N)
  for i, row in enumerate(grid):
    for j, value in enumerate(row):
      graph.insert(i, j, value)

  mc = graph.get_mario()
  graph.draw()

  parent = {}
  queue = []
  queue.append(mc)
  while queue:
    node = queue.pop(0)
    if node.value == "p":
      return backtrace(parent, mc, node)
    for adjacent in graph.get_neighbors(node):
      if node not in queue:
        parent[adjacent] = node  # <<<<< record its parent
        queue.append(adjacent)

def backtrace(parent, start, end):
    path = [end]
    while path[-1] != start:
      path.append(parent[path[-1]])
    path.reverse()

    word_path = []
    for index in range(len(path)-1):
      word_path.append(check_direction(path[index], path[index+1]))
    return word_path

def check_direction(cell_one, cell_two):
  if cell_one.c < cell_two.c:
    return "RIGHT"
  elif cell_one.c > cell_two.c:
    return "LEFT"
  elif cell_one.r < cell_two.r:
    return "DOWN"
  else:
    return "UP"

def validate_grid(N, grid):
  if len(grid) <= 1 or N <= 1:
    raise Exception("Grid not sufficiently large")
  if N != len(grid):
    raise Exception("Grid size does not match the length provided N")

  mario_check(grid)
  princess_check(grid)


def princess_check(grid):
  PRINCESS_FLAG = False
  for row in grid:
    if 'm' in list(row):
      PRINCESS_FLAG = True
  if not PRINCESS_FLAG:
    raise Exception("Princess not found in grid")


def mario_check(grid):
  MARIO_FLAG = False
  for row in grid:
    if 'm' in list(row):
      MARIO_FLAG = True
  if not MARIO_FLAG:
    raise Exception("Mario not found in grid")



