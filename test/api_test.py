import unittest
import json
from api import app



class MyTestCase(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    self.app = app.test_client()
    self.assertEqual(app.debug, False)

  # executed after each test
  def tearDown(self):
    pass

  """Home Page return 200 on Success"""

  def test_main_page(self):
    response = self.app.get('/', follow_redirects=True)
    self.assertEqual(200, response.status_code)

  """Log Page return 200 on Success"""
  def test_log_page(self):
    response = self.app.get('/log', follow_redirects=True)
    self.assertEqual(200, response.status_code)

  def test_simple_problem(self):
    response = self.app.get('/mario/3/m--,-p-,---', follow_redirects=True)
    self.assertEqual(200, response.status_code)
    json_data = json.loads(response.data.decode('utf-8'))
    pp = [tuple(n) for n in json_data]
    self.assertEqual([('DOWN', 'RIGHT'), ('RIGHT', 'DOWN')], pp)

  def test_more_paths(self):
    response = self.app.get('/mario/3/m--,---,--p', follow_redirects=True)
    self.assertEqual(200, response.status_code)
    json_data = json.loads(response.data.decode('utf-8'))
    pp = [tuple(n) for n in json_data]
    self.assertEqual([('DOWN', 'DOWN', 'RIGHT', 'RIGHT'), ('DOWN', 'RIGHT', 'DOWN', 'RIGHT'),
                      ('DOWN', 'RIGHT', 'RIGHT', 'DOWN'), ('RIGHT', 'DOWN', 'DOWN', 'RIGHT'),
                      ('RIGHT', 'DOWN', 'RIGHT', 'DOWN'), ('RIGHT', 'RIGHT', 'DOWN', 'DOWN')], pp)

  def test_many_obstacles(self):
    response = self.app.get('/mario/5/-----,-xxx-,mxxxp,-xxx-,-----', follow_redirects=True)
    self.assertEqual(200, response.status_code)
    json_data = json.loads(response.data.decode('utf-8'))
    pp = [tuple(n) for n in json_data]
    self.assertEqual([('UP', 'UP', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN'),
                      ('DOWN', 'DOWN', 'RIGHT', 'RIGHT', 'RIGHT', 'RIGHT', 'UP', 'UP')], pp)

  def test_mario_with_wrong_nsize(self):
    response = self.app.get('/mario/2/m--,-p-,---', follow_redirects=True)
    self.assertEqual(200, response.status_code)
    self.assertEqual("Oops! That was not a valid grid. Try again", response.data.decode('utf-8'))

  def test_mario_with_too_small_grid(self):
    response = self.app.get('/mario/1/-', follow_redirects=True)
    self.assertEqual("Oops! That was not a valid grid. Try again", response.data.decode('utf-8'))

  def test_no_mario(self):
    response = self.app.get('/mario/2/--,-p', follow_redirects=True)
    self.assertEqual("Oops! That was not a valid grid. Try again", response.data.decode('utf-8'))

  def test_no_princess(self):
    response = self.app.get('/mario/2/-m,--', follow_redirects=True)
    self.assertEqual("Oops! That was not a valid grid. Try again", response.data.decode('utf-8'))

  def test_no_grid(self):
    response = self.app.get('/mario/2/', follow_redirects=True)
    self.assertEqual(404, response.status_code)

  def test_no_size(self):
    response = self.app.get('/mario/-m,--', follow_redirects=True)
    self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()
