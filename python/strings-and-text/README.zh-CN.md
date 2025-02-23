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

## 合并和连接字符串

## 在字符串中插入变量

## 将文本格式化为固定列数

## 处理文本中的 HTML 和 XML 实体

## 对文本进行标记化

## 编写简单的递归下降解析器

## 对字节字符串执行文本操作
