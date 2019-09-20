import unittest
from api.__init__ import app


class MyTestCase(unittest.TestCase):
  def setUp(self):
    app.config['TESTING'] = True
    app.config['DEBUG'] = False
    self.assertEqual(app.debug, False)

  # executed after each test
  def tearDown(self):
    pass

  """Home Page return 200 on Success"""

  def test_main_page(self):
    response = app.get('/', follow_redirects=True)
    assertEqual(200, response.status_code)

  """Search Page return 200 on Success"""

  def test_mario_page(self):
    response = app.get('/mario/3/m--,-p-,---', follow_redirects=True)
    assertEqual(200, response.status_code)

  def test_mario_with_wrong_nsize_page(self):
    response = app.get('/mario/2/m--,-p-,---', follow_redirects=True)
    assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
