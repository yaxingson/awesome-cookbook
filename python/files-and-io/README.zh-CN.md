# 目录

## 读取和写入文本数据

针对不同的文本编码实现文件的读写操作:

```py
import sys
from urllib.request import urlopen

with open('./external/the-zen-of-python.txt', 'rt') as f:
  # data = f.read()
  for line in f:
    pass

with urlopen('https://jsonplaceholder.typicode.com/users') as res:
  with open('./external/users.json', 'wt') as f:
    print(res.read().decode('utf-8'), file=f)

# 获取系统默认的文本编码方式
default_encoding = sys.getdefaultencoding()

print(default_encoding)

f = open('./external/users.json', 'rt')

data = f.read()

# 手动关闭文件
f.close()

```

常见的文件编码方式:

- ASCII
- Latin-1
- UTF-8
- UTF-16

默认情况下，Python工作在“通用型换行符”模式下，即读取文件时将换行符转换为单独的`\n`字符:

```py
with open('./external/the-zen-of-python.txt', 'rt') as f:
  first_line = f.readlines()[0]
  print(repr(first_line)) # 'The Zen of Python, by Tim Peters\n'

with open('./external/the-zen-of-python.txt', 'rt', newline='') as f:
  first_line = f.readlines()[0]
  print(repr(first_line)) # 'The Zen of Python, by Tim Peters\r\n'

```

为`open()`函数提供可选的`errors`参数处理可能出现的编码错误:

```py
file_path = './external/the-zen-of-python-chinese.txt'

with open(file_path, 'rt', encoding='ascii', errors='ignore') as f:
  try:
    data = f.read()
    print(data)
  except UnicodeDecodeError:
    pass

```

> 关于文本，第一守则是只需确保总是采用正确的文本编码形式即可

## 打印到文件

将`print()`函数的输出重定向到文件中:

```py
from json import dumps

todos = [
  {
    'user_id':1, 
    'id':1, 
    'title':'dejects aut ante', 
    'completed':False
  },
  {
    'user_id':1, 
    'id':2, 
    'title':'quic ut nam facials et officio qui', 
    'completed':True
  },
  {
    'user_id':1, 
    'id':3, 
    'title':'fiat venial minus', 
    'completed':False
  },
]

with open('./external/todos.json', 'wt') as f:
  print(dumps(todos), file=f)


```

## 使用不同的分隔符或行结束符打印

通过`print()`函数输出数据时，修改分隔符或行结尾符:

```py
print('Mabel Clarke', 50, 91.5, sep=',') # Mabel Clarke,50,91.5
print('Mabel Clarke', 50, 91.5, sep=',', end='!!\n') # 'Mabel Clarke,50,91.5!!\n'

# 禁止打印换行符
for i in range(1, 6):
  print(i, end=' ')

```

## 读取和写入二进制数据

读写图像、声音等二进制数据文件:

```py
with open('./external/bear.jpg', 'rb') as f:
  data = f.read()
  print(data)

# 在做索引和迭代操作时，字节串会返回代表该字节的整数值
b = b'hello,world'

print(b[0]) # 104

for c in b:
  print(c)

```

写入的二进制数据可以是字节串、`bytearray`对象、数组或C结构体等:

```py
import array

numbers = array.array('i', range(10))

with open('./external/data.bin', 'wb') as f:
  f.write(numbers)

values = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

with open('./external/data.bin', 'rb') as f:
  f.readinto(values)

print(values) # array('i', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

```

> 内存缓存区

## 写入一个尚不存在的文件

只有写入数据的文件不存在文件系统中时，才会写入数据:

```py
import os

try:
  with open('./external/data.bin', 'xb') as f:
    f.write(b'hello,world')
except FileExistsError:
  pass


if not os.path.exists('./external/data.bin'):
  with open('./external/data.bin', 'wb') as f:
    f.write(b'hello,world')
else:
  print('File already exists!')

```

## 在字符串上执行 I/O 操作

使用`io.StringIO`和`io.ByteIo`类创建类似文件的对象:

```py
from io import StringIO, BytesIO

s = StringIO()

s.write('hello,world\n')
print('this is a test', file=s, end='')

print(repr(s.getvalue())) # 'hello,world\nthis is a test'

s = StringIO('hello\nworld\n')

print(s.read(4)) # hell
print(repr(s.read())) # 'o\nworld\n'

```

## 读取和写入压缩数据文件

读写以`gzip`或`bz2`格式压缩的文件数据:

```py
import gzip
import bz2

# gzip压缩
with gzip.open('./external/the-zen-of-python.txt.gz', 'rt') as f:
  text = f.read()
  print(text)

# bz2压缩
with bz2.open('./external/the-zen-of-python.txt.bz2', 'rt') as f:
  text = f.read()
  print(text)

# 通过可选的compresslevel参数指定压缩级别
with gzip.open('./external/index.html.gz', 'wt', compresslevel=5) as f:
  tpl = [
    '<!DOCTYPE html>',
    '<html>',
    '<head></head>',
    '<body>',
    '',
    '</body>',
    '</html>'
  ]

  f.write('\n'.join(tpl))

```

`gzip.open()`和`bz2.open()`能够对已经以二进制模式打开的文件进行叠加操作:

```py
import gzip

f = open('./external/index.html.gz', 'rb')

with gzip.open(f, 'rt') as g:
  text = g.read()
  print(text)

f.close()

print(f.closed)

```

## 迭代固定大小的记录

## 将二进制数据读取到可变缓冲区

## 内存映射二进制文件

## 操作路径名

## 测试文件是否存在

## 获取目录列表

## 绕过文件名编码

## 打印无效文件名

## 添加或更改已打开文件的编码

## 将字节写入文本文件

## 将现有文件描述符包装为文件对象

## 创建临时文件和目录

## 与串口通信

## 序列化 Python 对象
