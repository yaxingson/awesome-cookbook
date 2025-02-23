import os
from urllib.request import urlopen

url = 'https://github.com/reworkd/AgentGPT'
filename = 'README.zh-CN.md'

print(url.startswith('https'))
print(filename.endswith('.md'))

files = os.listdir('.')

# `startswith`和`endswith`的第一个参数只能是字符串或元组类型
print([name for name in files if name.endswith(('.md'))])

def read_data(path:str):
  if path.startswith(('http:', 'https:', 'ftp:')):
    return urlopen(path).read()
  else:
    with open(path) as f:
      return f.read()

print(read_data('https://httpbin.org/get'))
