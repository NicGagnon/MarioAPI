from unittest import TestCase
from app import find_shortest_path

class myTestCase(TestCase):
  def test_basic_case(self):
    path = find_shortest_path(3, ['--m','-x-','-p-'])
    self.assertEqual([('DOWN', 'DOWN', 'LEFT')], path)

