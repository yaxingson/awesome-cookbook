# 目录

## 测试输出发送到标准输出

> 测试驱动开发（TDD）

利用`unittest.mock`模块中的`patch()`函数为单独的测试用例模拟标准输出:

```py
from io import StringIO
from datetime import datetime
from unittest.mock import patch
from unittest import TestCase, main

def get_date_time(datetime):
  date = f'{datetime.year}-{datetime.month:02}-{datetime.day:02}'
  time = f'{datetime.hour:02}:{datetime.minute:02}:{datetime.second:02}'
  return date, time

def log(msg, *, format='%L %D %T', level='INFO'):
  now = datetime.now()
  date, time = get_date_time(now)

  prefix = format.replace('%D', date).replace('%T', time).replace('%L', f'[{level.upper()}]')

  print(f'{prefix} {msg}')

class TestLog(TestCase):
  def test_log_msg_to_stdout(self):
    now = datetime.now()
    date, time = get_date_time(now)

    expected_url = f'[ERROR] {date} {time} division by zero\n'

    with patch('sys.stdout', new=StringIO()) as fake_out:
      log('division by zero', level='error')
      self.assertEqual(fake_out.getvalue(), expected_url)    

main()

```

> 哑值

## 在单元测试中修补对象

使用`unittest.mock.patch()`函数为对象添加补丁:

```py
from unittest import TestCase, main
from unittest.mock import patch

url = 'https://chat.deepseek.com/a/chat'

def parse_url(url):
  return {}

# 单独使用（手动打补丁）
p = patch('__main__.parse_url')
mock_func = p.start()

parse_url(url)
mock_func.assert_called_with(url)

p.stop()

# 装饰器
@patch('__main__.parse_url')
def test_parse_url(url, mock_func):
  parse_url(url)
  mock_func.assert_called_with(url)

test_parse_url(url)

# 上下文管理器
with patch('__main__.parse_url') as mock_func:
  parse_url(url)
  mock_func.assert_called_with(url)

```

将装饰器或上下文管理器堆叠起来为多个对象打补丁:

```py
from unittest.mock import patch

def parse_url():
  pass

def random_int():
  pass

def patch_flags():
  pass

def test():
  with patch('__main__.parse_url') as m1, \
      patch('__main__.random_int') as m2, \
      patch('__main__.patch_flags') as m3:
    print(parse_url)

test()

```


## 在单元测试中测试异常条件

```py
import re
import errno
from unittest import TestCase, main

def parse_url(url:str):
  if not re.match('https?', url):
    raise ValueError('invalid url!')

class TestException(TestCase):
  def test_parse_url(self):
    self.assertRaises(ValueError, parse_url, 'file://')

  def test_parse_invalid_url(self):
    self.assertRaisesRegex(ValueError, 'invalid.*', parse_url, '')

  def test_file_not_found(self):
    try:
      open('')
    except IOError as e:
      # 检查异常的值
      self.assertEqual(e.errno, errno.ENOENT)
    else:
      self.fail('IOError not raised')

main()

```

## 将测试输出记录到文件

```py
import sys
from unittest import TestCase, TestLoader, TextTestRunner

def main(out=sys.stderr, verbosity=2):
  loader = TestLoader()  
  
  # 组装测试套件
  # suite = loader.loadTestsFromModule(sys.modules[__name__])
  suite = loader.loadTestsFromTestCase(TestStrMethod)

  # 运行包含在测试套件中的测试用例
  TextTestRunner(out, verbosity=verbosity).run(suite)

class TestStrMethod(TestCase):
  def test_upper(self):
    self.assertEqual('python'.upper(), 'PYTHON')
  
  def test_lower(self):
    self.assertEqual('Testing'.lower(), 'testING')

with open('./external/testing.log', 'w') as f:
  main(f)

```

## 跳过或预期测试失败

将`unittest`模块中的装饰器作用在测试方法上，以此控制它们的处理行为:

```py
import os
import platform
from unittest import TestCase, skip, skipIf,\
  skipUnless, expectedFailure, main

class TestBuiltinFunctionOrMethod(TestCase):
  def test_hex(self):
    self.assertTrue(hex(255) == '0xff')

  @skip('skipped test')
  def test_max(self):
    self.fail('should have failed!')

  @skipIf(os.name == 'posix', 'Not supported on Unix')
  def test_print(self):
    import winreg

  @skipUnless(platform.system() != 'Windows', 'Mac specific test')
  def test_abs(self):
    self.assertFalse(True)

  @expectedFailure
  def test_callable(self):
    self.assertEqual(2**3, 8)

main(verbosity=2)

```

用来跳过检查的装饰器同样也可以作用在整个测试类上:

```py
@skipUnless(platform.system() == 'Linux', 'Linux specific test')
class TestBuiltinFunctionOrMethod(TestCase):
  pass

```

## 处理多个异常

```py
import errno
from logging import Logger

logger = Logger('default')

try:
  # open()
  # open('/')
  open('/d/pictures/')
# 指定一个基类捕获所有异常
except OSError as e:
  if e.errno == errno.ENOENT:
    logger.error('File not found')
  elif e.errno == errno.EACCES:
    logger.error('Permission denied')
  else:
    logger.error('Unexpected error: %d', e.errno)
except (PermissionError, FileNotFoundError):
  pass
except TypeError:
  pass

```

> 通过检查异常的`__mro__`属性可以查阅某个特定异的类层次结构

## 捕获所有异常

捕获除了`SystemExit`、`KeyboardInterrupt`和`GeneratorExit`之外的所有异常:

```py
from logging import Logger

logger = Logger('exception')

try:
  pass
except Exception as e:
  # 针对异常产生的实际原因做日志记录或报告，提供诊断信息
  logger.error(e)
  # raise

```

## 创建自定义异常

通过继承`Exception`类或其他已有的异常类型创建新的异常类:

```py
class NetworkError(Exception):
  def __init__(self, message, code, reason):
    # 请确保总是用所有传递过来的参数调用`Exception.__init__()`，且所有参数会
    # 以元组的形式保存在新创建异常类实例的`.args`属性上
    super().__init__(message, code, reason)
    self.code = code
    self.reason = reason

class OfflineError(NetworkError):
  pass

class ProtocolError(NetworkError):
  pass

class CrossOriginError(NetworkError):
  pass


def request():
  pass

try:
  request()
except NetworkError as e:
  pass
except OfflineError:
  pass
except ProtocolError:
  pass

try:
  raise NetworkError('Oh, no!', 10291, 'no network connection')
except NetworkError as e:
  print(e.args)

```

> `BaseException`是预留给系统退出异常的，比如`KeyboardInterrupt`和
> `SystemExit`，以及其他应该通知应用程序退出的异常

## 在响应另一个异常时引发异常

引发一个异常作为捕获另一个异常时的响应，且在traceback回溯中包含这两个异常的信息:

```py
def div(x, y):
  try:
    return x / y
  except ZeroDivisionError as e:
    # raise RuntimeError('A parsing error occurred!') from e
    
    # 产生隐式的异常链
    # print([][1]) 

    # 阻止异常链的产生
    raise RuntimeError('A parsing error occurred!') from None

try:
  div(1, 0)
except RuntimeError as e:
  if(e.__cause__):
    # 查看异常对象的`__cause__`属性来跟踪所希望的异常链
    print(e.__cause__)
except IndexError as e:
  if(e.__context__):
    print(e.__context__)

```

> 大部分情况下，在except块中使用raise语句时，应采用`raise from`语句显式将异常产生的原因串联起来

## 重新引发最后一个异常

使用单独的`raise`语句重新抛出异常:

```py
try:
  int('N/A')
except ValueError:
  raise

```

## 发出警告消息

使用`warnings.warn()`函数产生告警信息:

```py
# buffer.py
from warnings import warn

class Buffer:
  def __init__(self):
    messages = [
      'Buffer() is deprecated due to security and usability issues.', 
      'Please use the Buffer.alloc() or Buffer.allocUnsafe() methods instead'  
    ]
    warn(''.join(messages), DeprecationWarning)

  @staticmethod
  def alloc():
    pass

  @staticmethod
  def allocUnsafe():
    pass

Buffer()

```

告警类别:

- `UserWarning`
- `DeprecationWarning`
- `SyntaxWarning`
- `RuntimeWarning`
- `ResourceWarning`
- `FutureWarning`

对告警信息的处理取决于如何执行解释器及其他配置:

```sh
$ python -W all buffer.py

# 使用`-W error`选项将告警信息转换为异常
$ python -W error buffer.py

# 忽略所有的告警
$ python -W ignore buffer.py

```

应用示例:

```py
from warnings import simplefilter

# 控制告警信息的输出，可选参数值: always、ignore和error
simplefilter('always')

f = open('./external/motto.txt')

# f.close()

del f

```

## 调试基本程序崩溃

```sh
$ python -i program.py

```

在交互式shell环境下加载Python调试器:

```
Traceback (most recent call last):
  File "python/testing-debugging-and-exceptions/catching-all-exceptions.py", line 4, in <module>
    plus('', 0)
  File "python/testing-debugging-and-exceptions/catching-all-exceptions.py", line 2, in plus
    return x + y
TypeError: can only concatenate str (not "int") to str
>>> plus
<function plus at 0x000001EE9D0DE160>
>>> import pdb
>>> pdb.pm()
> d:\workspace\repository\github\awesome-cookbook\python\testing-debugging-and-exceptions\catching-all-exceptions.py(2)plus()
-> return x + y
(Pdb) w
  d:\workspace\repository\github\awesome-cookbook\python\testing-debugging-and-exceptions\catching-all-exceptions.py(4)<module>()
-> plus('', 0)
> d:\workspace\repository\github\awesome-cookbook\python\testing-debugging-and-exceptions\catching-all-exceptions.py(2)plus()
-> return x + y
(Pdb) print x, y
*** SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x, y)?
(Pdb) print(x, y)
 0
(Pdb) x, y
('', 0)
(Pdb) q
>>> ^Z

```

当代码在难以获取交互式shell的环境中运行时，通常可以捕获错误并手动生成traceback回溯:

```py
import traceback
import sys
from operator import add

try:
  add('', 0)
except:
  print('***** AN ERROR OCCURRED *****')
  traceback.print_exc(file=sys.stdout)

```

打印程序的调用栈信息或手动加载调试器:

```py
import traceback
import sys
import pdb

def once(func):
  called = False
  def inner(*args, **kwargs):
    nonlocal called
    if not called:
      # 打印函数调用栈信息
      # traceback.print_stack(file=sys.stdout)
      
      # 加载调试器
      pdb.set_trace()

      func(*args, **kwargs)
    called = True
  return inner

def init():
  print('***** START INIT *****')

init = once(init)

init()
init()
init()

```

## 对程序进行性能分析和计时

使用UNIX下的`time`命令对整个程序做计时统计:

```sh
$ time python script.py

```

利用`cProfile`模块针对程序的行为产生一份详细报告:

```sh
$ python -m cProfile script.py

```

使用装饰器对函数进行性能分析:

```py
import time
from functools import wraps

def time_statistics(fn):
  @wraps(fn)
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    return_val = fn(*args, **kwargs)
    end = time.perf_counter()
    print(f'{fn.__module__}.{fn.__name__}: {end - start}')
    return return_val

  return wrapper

@time_statistics
def countdown(n):
  while n > 0:
    n -= 1

countdown(100000)

```

通过上下文管理器对程序中的代码块进行计时统计:

```py
import time
from contextlib import contextmanager

@contextmanager
def time_statistics(label):
  start = time.perf_counter()
  try:
    yield
  finally:
    end = time.perf_counter()
    print(f'{label}: {end - start}')

with time_statistics('countdown'):
  n = 100000
  while n > 0:
    n -= 1

```

利用`timeit`模块对短小的代码片段做性能统计:

```py
from timeit import timeit

print(timeit('sqrt(2)', 'from math import sqrt', number=100000))

```

> 墙上时间和进程时间

## 让程序运行得更快

> JIT即时编译器

优化原则:

1. 不要过早优化，首先确保程序能够正常工作
2. 仅针对已知的性能瓶颈做优化，比如内层循环

微优化：指对代码进行小规模的性能优化，通常是为了提高执行效率或减少资源消耗

优化技术:

### 使用函数

```py
#!/usr/bin/env python
import sys
import csv

def read_csv(filename):
  with open(filename) as f:
    for row in csv.reader(f):
      print(row)

read_csv(sys.argv[1])

```

> 定义在全局范围内的代码运行起来比定义在函数中的代码慢，其速度差异与局部变量和全局变量的实现机制有关

### 有选择性的消除属性访问

```py
import timeit
import math

def compute_roots_v1(nums):
  result = []
  for n in nums:
    result.append(math.sqrt(n))
  return result

def compute_roots_v2(nums):
  sqrt = math.sqrt
  result = []
  result_append = result.append
  for n in nums:
    result_append(sqrt(n))
  return result

nums = range(10)

def test():
  for n in range(10):
    r = compute_roots_v1(nums)

print(timeit.timeit(test, number=10**5))

```

适用于频繁执行代码的场景，比如循环等

### 理解变量所处的位置

在内层循环中将需要经常访问的属性移到局部变量中:

```py
class SomeClass:
  def method(self):
    val = self.value
    for x in s:
      op(val)

```

### 避免不必要的抽象

任何时候使用额外的处理层比如装饰器、属性或者描述符包装代码时，代码的运行速度就会变慢

```py
from timeit import timeit

class A:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  @property
  def y(self):
    return self.__y

  @y.setter
  def y(self, value):
    self.__y = value

a = A(1, 0)

print(timeit('a.x', 'from __main__ import a'))
print(timeit('a.y', 'from __main__ import a'))

```

### 使用内建的容器

> 内建的数据结构（字符串、元组、列表、集合以及字典）都是用C语言实现的，速度非常快

### 避免产生不必要的数据结构或拷贝动作

```py
squares = [x*x for x in sequence]

```
> 共享值

