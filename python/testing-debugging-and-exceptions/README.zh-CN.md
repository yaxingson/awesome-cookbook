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

## 在响应另一个异常时引发异常

## 重新引发最后一个异常

使用单独的`raise`语句重新抛出异常:

```py
try:
  int('N/A')
except ValueError:
  raise

```

## 发出警告消息

## 调试基本程序崩溃

## 对程序进行性能分析和计时

## 让程序运行得更快
