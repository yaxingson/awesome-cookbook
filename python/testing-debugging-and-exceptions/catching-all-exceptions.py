from urllib.request import urlopen
from unittest import TestCase, main
from unittest.mock import Mock

# https://m.douban.com/rexxar/api/v2/subject/recent_hot/movie?start=20&limit=20&category=%E7%83%AD%E9%97%A8&type=%E5%8D%8E%E8%AF%AD

def down_movies():
  url = 'https://jsonplaceholder.typicode.com/todos'
  u = urlopen(url)
  print(u.read())
  

class TestMock(TestCase):
  def test_down_movies(self):
    pass

if __name__ == '__main__':
  down_movies()
