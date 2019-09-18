# Author is Nicolas Gagnon 2019
from graph import Graph


def find_shortest_path(N, grid):
  validate_grid(N, grid)

  # Mark all the vertices as not visited
  visited = [False] * N * N
  graph = Graph(N)

  for i, row in enumerate(grid):
    for j, value in enumerate(row):
      graph.insert(i, j, value)

  graph.draw()


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



