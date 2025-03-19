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

```py
from subprocess import check_output, \
  CalledProcessError, TimeoutExpired, STDOUT
from shlex import quote

try:
  # 使用`stderr`参数获取标准输出和标准错误输出
  out_bytes = check_output(['ls', '-a'], stderr=STDOUT)
  
  # 执行带有超时机制的命令
  out_bytes = check_output(['cmd'], timeout=5)

  # 通过shell执行涉及管道、I/O重定向或其他复杂的命令
  out_bytes = check_output(['grep python | wc > out'], shell=True)

  print(out_bytes.decode())
except CalledProcessError as e:
  out_bytes = e.output
  code = e.returncode
  print(out_bytes, code)
except TimeoutExpired as e:
  pass

```

> 在shell下执行命令存在安全威胁，特别是当参数来自于用户输入

同一个子进程通信:

```py
from subprocess import Popen, PIPE

text = '''
hello world
this is a test
goodbye
'''

p = Popen(['wc'], stdout=PIPE, stdin=PIPE)

stdout, stderr = p.communicate(text.encode())

print(stdout.decode())
print(stderr and stderr.decode())

```

> TTY

## 复制或移动文件和目录

拷贝或移动文件和目录:

```py



```


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

读取`.ini`格式的配置文件:

```py
import sys
from configparser import ConfigParser

cfg = ConfigParser()

cfg.read('./external/config.ini')

print(cfg.sections())
print(cfg.get('Installation', 'include'))
print(cfg.getint('Network', 'timeout'))
print(cfg.getboolean('Network', 'usessl'))

cfg.set('Network', 'timeout', '1000')
cfg.set('Database', 'username', 'admin')

with open('./external/config.ini', 'w') as f:
  cfg.write(f, space_around_delimiters=True)

```


## 向简单脚本添加日志记录

## 向库添加日志记录

## 制作秒表计时器

```py
import time
class Timer:
  # `time.perf_counter`函数总是会使用系统重精度最高的计时器
  def __init__(self, func=time.perf_counter):
    self.elapsed = 0.0
    self._func = func
    self._start = None

  def start(self):
    if self._start is not None:
      raise RuntimeError('Already started')
    self._start = self._func()

  def stop(self):
    if self._start is None:
      raise RuntimeError('Not started')
    end = self._func()
    self.elapsed += end - self._start
    self._start = None

  def reset(self):
    self.elapsed = 0.0

  def __enter__(self):
    self.start()
    return self

  def __exit__(self, *args):
    self.stop()

  @property
  def running(self):
    return self._start is not None

def countdown(n):
  while n > 0:
    n -= 1

# 获取进程的CPU时间
t = Timer(func=time.process_time)

t.start()
countdown(10000000)
t.stop()

print(t.elapsed)

with Timer() as t:
  countdown(10000000)
print(t.elapsed)

```

> 系统时间和进程时间

## 对内存和CPU使用设置限制

使用`resource`模块对运行在`UNIX`系统上的程序在内存和CPU的使用量上设定限制:

```py
import signal
import resource
import os

# 限制CPU时间
def set_max_runtime(seconds):
  def time_exceeded(*args):
    raise SystemExit(1)
  soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
  resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
  signal.signal(signal.SIGXCPU, time_exceeded)

set_max_runtime(10)

while True:
  pass


```

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
