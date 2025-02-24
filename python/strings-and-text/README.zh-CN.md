# 目录

## 在多个分隔符上拆分字符串

```py
import re

line = 'agent-gpt allows; you, to,configure,  and'

print(re.split(r'[;,\s]\s*', line))

# 当正则表达式模式中包含捕获组时，最终结果也会包含匹配的文本
fields = re.split(r'(;|,|\s)\s*', line)

print(fields)

# 使用非捕获组（?:）
fields = re.split(r'(?:;|,|\s)\s*', line)

print(fields)


```

## 匹配字符串的开头或结尾

```py
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

```


## 使用 Shell 通配符模式匹配字符串

UNIX Shell下的通配符匹配:

```py
from fnmatch import fnmatch, fnmatchcase

# `fnmatch()`匹配模式的大小写区分规则和操作系统的底层文件系统相同
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

# `fnmatchcase()`匹配模式的大小写区分规则和操作系统的底层文件系统无关
print(fnmatchcase('foo.txt', '*.TXT'))

```

> 编写匹配文件名的代码时应使用`glob`模块

## 匹配和搜索文本模式

```py



```


## 搜索和替换文本

## 搜索和替换不区分大小写的文本

## 为最短匹配指定正则表达式

## 为多行模式编写正则表达式

## 将 Unicode 文本标准化为标准表示

## 在正则表达式中处理 Unicode 字符

## 从字符串中剥离不需要的字符

## 清理和整理文本

## 对齐文本字符串

以某种对齐方式对文本做格式化处理:

```py
text = 'hello,world'

print(repr(text.ljust(30))) # 'hello,world                   '
print(repr(text.rjust(30))) # '                   hello,world'
print(repr(text.center(30)))  # '         hello,world          '

print(text.ljust(30, '*')) # hello,world*******************

print(format(text, '<30'))
print(format(text, '>30'))
print(format(text, '^30'))

print(format(text, '*<30'))

# 字符串的`format()`方法格式化多个值
print('{:>10s} {:>10s}'.format('hello', 'world'))

# `format`函数可以作用于任何值
print(repr(format(1.2345, '^10.2f'))) # '   1.23   '

# 利用%操作符格式化文本
print(repr('%-30s'%text)) # 'hello,world                   '
print(repr('%30s'%text)) # '                   hello,world'

```

## 合并和连接字符串

## 在字符串中插入变量

将字符串中嵌入的变量名称以变量的字符串值的形式替换掉:

```py
s = '{name} has {n} messages'

print(s.format(name='Earl Goodwin', n=37))

# 当前作用域存在字符串中的变量名时
name = 'Earl Goodwin'
n = 37

print(s.format_map(vars()))

class Info:
  def __init__(self, name, n):
    self.name = name
    self.n = n

# `vars()`函数作用在类实例上
print(s.format_map(vars(Info('Earl Goodwin', 37))))

```

定义带有`__miss__()`方法的字典类解决缺少某个值时报错的问题:

```py
import sys

s = '{name} has {n} messages'

try:
  s.format(name='Jeanette Hodges')
except KeyError as e:
  print(f'{type(e).__name__}: {e}')

class SafeSub(dict):
  def __missing__(self, key):
    return f'{{ {key} }}'

name = 'Martha Clark'

print(s.format_map(SafeSub(vars()))) # Martha Clark has { n } messages

def template(text):
  return text.format_map(SafeSub(sys._getframe(1).f_locals))

print(template('Hello, {name}!')) # Hello, Martha Clark!
print(template('Your favorite color is {color}')) # Your favorite color is { color }

```

> `frame hack`技巧: 需要同函数的栈帧打交道 

字符串格式化操作:

```py
import string

name = 'Jerome Edwards'
n = 37

s = string.Template('$name has $n messages.')

print(s.substitute(vars()))

```

## 将文本格式化为固定列数

以指定的列数格式化长字符串:

```py
import textwrap

s = '''
In the heart of the bustling city, where skyscrapers kissed the clouds 
and streets buzzed with life, there existed a small, hidden café. Tucked 
away in a quiet alley, it was a sanctuary for those seeking solace from 
the chaos. The aroma of freshly brewed coffee mingled with the scent of 
warm pastries, creating an inviting atmosphere. Patrons, ranging from weary 
office workers to curious travelers, found comfort in the cozy corners and 
soft jazz melodies that filled the air. It was more than just a café; it 
was a place where stories were shared, dreams were whispered, and time 
seemed to slow down, if only for a moment.
'''

print('=' * 80)
print(textwrap.fill(s, 70))
print('=' * 80)
print(textwrap.fill(s, 40))
print('=' * 80)
print(textwrap.fill(s, 40, initial_indent=' '))
print('=' * 80)
print(textwrap.fill(s, 40, subsequent_indent=' '))
print('=' * 80)

```

获取终端的尺寸大小:

```py
import os

print(os.get_terminal_size().columns)

```

## 处理文本中的 HTML 和 XML 实体

转义HTML或XML中的特殊字符:

```py
import html

s = 'elements are written as "<tag>text</tag>"'

print(html.escape(s)) 
# Output: elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;&quot;

print(html.escape(s, quote=False))
# Output: elements are written as "&lt;tag&gt;text&lt;/tag&gt;"

# 将字符串中的非ASCII字符对应的字符编码实体嵌入到编码后的字节串中
s = 'Spicy Jalapeño'

print(s.encode('ascii', errors='xmlcharrefreplace')) # b'Spicy Jalape&#241;o'

```

利用HTML或XML解析器自带的功能函数和方法转义文本中的实体:

```py
from html import unescape
from html.parser import HTMLParser
from xml.sax.saxutils import unescape as xml_unescape

s = 'Spicy &quot;Jalape&#241;o&quot'

parser = HTMLParser()

print(parser.unescape(s)) # Spicy "Jalapeño"
print(unescape(s)) # Spicy "Jalapeño"

t = 'the prompt is &gt;&gt;&gt;'

print(xml_unescape(t)) # the prompt is >>>

```

## 对文本进行标记化

将字符串文本解析为标记流:

```py
import re
from collections import namedtuple

text = 'expr = 23 + 42 * 10'

# 通过正则表达式中的命名捕获组定义出所有可能的标记，包括空格
NAME = r'(?P<NAME>[a-zA-Z_]\w*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pattern = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# 创建扫描对象
scanner = master_pattern.scanner(text)

m1 = scanner.match()
print((m1.lastgroup, m1.group())) # ('NAME', 'expr')

m2 = scanner.match()
print((m2.lastgroup, m2.group())) # ('WS', ' ')

m3 = scanner.match()
print((m3.lastgroup, m3.group())) # ('EQ', '=')

# 利用生成器函数重构代码
Token = namedtuple('Token', ('type', 'value'))

def generate_tokens(pattern, text):
  scanner = pattern.scanner(text)
  for m in iter(scanner.match, None):
    yield Token(m.lastgroup, m.group())

print(list(generate_tokens(master_pattern, text)))

```

`re`模块会按照指定的顺序对模式做匹配，当某个模式是另一个较长模式的子串时，应确保较长的模式先做匹配:

```py
import re

text = 'year <= 2025'

NAME = r'(?P<NAME>[a-zA-Z_]\w*)'
NUM = r'(?P<NUM>\d+)'
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

correct_pattern = re.compile('|'.join([NAME, NUM, LE, LT, EQ, WS]))
incorrect_pattern = re.compile('|'.join([NAME, NUM, LT, LE, EQ, WS]))

scanner = correct_pattern.scanner(text)

for m in iter(scanner.match, None):
  print((m.lastgroup, m.group()))

```


## 编写简单的递归下降解析器

## 对字节字符串执行文本操作

字节串上执行常见的文本操作:

```py
import re

data = b'hello,python'

print(data[0:5]) # b'hello'
print(data.startswith(b'hello')) # True
print(data.replace(b'hello', b'hi')) # b'hi,python'

# 字节数组
data = bytearray(data)

print(data[0:5]) # bytearray(b'hello')
print(data.split(b',')) # [bytearray(b'hello'), bytearray(b'python')]

# 当在字节串上执行正则表达式的模式匹配操作时，模式需要以字节串形式指定
pattern = b'[,]'

print(re.split(pattern, data)) # [b'hello', b'python']

# 字节串的索引值为ASCII码
print(data[0]) # 104
print(data[1]) # 101

# 将字节串解码为字符串
print(data.decode(encoding='ascii'))

```

字节串的格式化操作:

```py
print(b'%10s %10d %10.2f'%(b'hello', 100, 567.1))
print('{:>10s} {:10d} {:10.2f}'.format('hello', 100, 567.1).encode('ascii'))

```

当提供一个以字节编码的文件名时，文件系统通常会禁止对文件名的编码和解码:

```py
import os

with open('./external/hello\xf1o.txt', 'w') as f:
  f.write('hello,world')

print(os.listdir('./external')) # ['helloño.txt']
print(os.listdir('./external'.encode('ascii'))) # [b'hello\xc3\xb1o.txt']

```
