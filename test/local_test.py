from unittest import TestCase
from app import find_shortest_path


class myTestCase(TestCase):
  def test_basic_case(self):
    path = find_shortest_path(3, ['--m', '-x-', '-p-'])
    self.assertEqual([('DOWN', 'DOWN', 'LEFT')], path)

  def test_basic_with_uppercase(self):
    path = find_shortest_path(3, ['--M', '-X-', '-P-'])
    self.assertEqual([('DOWN', 'DOWN', 'LEFT')], path)

  def test_equal_distance_case(self):
    path = find_shortest_path(3, ['m--', '-p-', '---'])
    self.assertEqual([('DOWN', 'RIGHT'), ('RIGHT', 'DOWN')], path)

  def test_many_equal_distance_case(self):
    path = find_shortest_path(3, ['m--', '---', '--p'])
    self.assertEqual([('DOWN', 'DOWN', 'RIGHT', 'RIGHT'), ('DOWN', 'RIGHT', 'DOWN', 'RIGHT'),
                      ('DOWN', 'RIGHT', 'RIGHT', 'DOWN'), ('RIGHT', 'DOWN', 'DOWN', 'RIGHT'),
                      ('RIGHT', 'DOWN', 'RIGHT', 'DOWN'), ('RIGHT', 'RIGHT', 'DOWN', 'DOWN')], path)

  def test_many_obstacles(self):
    path = find_shortest_path(5, ['-----', '-xxx-', 'mxxxp', '-xxx-', '-----'])
    self.assertEqual([('UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN'),
                      ('DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP')], path)

  def test_no_matrix(self):
    self.assertRaises(Exception, find_shortest_path, 0, [''])

  def test_one_matrix(self):
    self.assertRaises(Exception, find_shortest_path, 1, ['-'])

  def test_no_mario_matrix(self):
    self.assertRaises(Exception, find_shortest_path, 2, ['--', '-p'])

  def test_no_princess_matrix(self):
    self.assertRaises(Exception, find_shortest_path, 2, ['m-', '--'])

  def test_inconsistent_size_matrix(self):
    self.assertRaises(Exception, find_shortest_path, 3, ['m-', '--'])

  def test_inconsistent_size_again_matrix(self):
    self.assertRaises(Exception, find_shortest_path, 2, ['m--', '---', '--p'])
