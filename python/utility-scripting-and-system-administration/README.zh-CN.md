# 目录

## 通过重定向、管道或输入文件接受脚本输入

将管道符、文件重定向或文件名作为脚本的输入:

```py
#!/usr/bin/env python
import fileinput

with fileinput.input() as f_input:
  for line in f_input:
    print(f'{f_input.filename()} {f_input.lineno():02} {line}', end='')

```

```sh
$ ls | ./script.py
$ ./script.py < README.md
$ ./script.py README.md

```

## 以错误消息终止程序

终止程序时向标准错误输出打印一条消息，并返回一个非零状态码:

```py
raise SystemExit('It failed!')

```

## 解析命令行选项

```py
#!/usr/bin/env python
import sys
import argparse

parser = argparse.ArgumentParser(description='Search some files')

parser.add_argument(dest='filenames', metavar='filename', nargs='*')

parser.add_argument('-p', '--pat', metavar='pattern', required=True, 
                    dest='patterns', action='append', help='text pattern to search for')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store_true', help='output file')
parser.add_argument('--speed', dest='speed', action='store', 
                    choices=['slow', 'fast'], default='slow', help='search speed')

args = parser.parse_args()

print(args)

```

> `getopt`和`optparse`模块


## 在运行时提示输入密码

使用`getpass`模块为用户提供脚本运行时的密码输入提示，且输入的密码不会显示在终端上:

```py
#!/usr/bin/env python
import getpass

# 根据用户shell环境中当前的用户登录名或以本地系统的密码数据库为支撑
user = getpass.getuser()
passwd = getpass.getpass()

if user == 'SGK' and passwd == '123456+':
  print('welcome')
else:
  print('invalid user or passwd')

```

## 获取终端大小

```py
import os

print(os.get_terminal_size())

```

## 执行外部命令并获取其输出

## 复制或移动文件和目录

## 创建和解压归档文件

使用`shutil`模块中的`make_archive`和`unpack_archive`函数创建或解包归档文件:

```py
from os import getcwd
from os.path import join
from shutil import make_archive, unpack_archive, get_archive_formats

# 获取所支持的归档格式列表
print(get_archive_formats())

print(make_archive('utility-scripting-and-system-administration', 'zip', '.', verbose=1, dry_run=True))

unpack_archive('utility-scripting-and-system-administration.zip')

```

> `tarfile`、`zipfile`、`gzip`和`bz2`模块

## 按名称查找文件

## 读取配置文件

## 向简单脚本添加日志记录

## 向库添加日志记录

## 制作秒表计时器

## 对内存和CPU使用设置限制

## 启动网页浏览器

以独立于平台的方式加载浏览器:

```py
import webbrowser

try:
  # 指定具体的浏览器
  chrome_path = '/c/Program Files (x86)/Google/Chrome/Application/chrome'
  browser = webbrowser.get(chrome_path)

  browser.open('https://www.python.org/')

except webbrowser.Error:
  pass

```
