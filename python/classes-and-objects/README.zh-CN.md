# 目录

## 更改实例的字符串表示

通过定义`__repr__`和`__str__`方法修改对象的字符串表示:

```py
class Pair:
  def __init__(self, first, second):
    self.first = first
    self.second = second

  def __repr__(self):
    return 'Pair({0.first!r}, {0.second!r})'.format(self)
  
  def __str__(self):
    return '({0.first!s}, {0.second!s})'.format(self)

  def __eq__(self, other):
    return self.first == other.first and self.second == other.second

p = Pair('Adrian Mann', 'wa@zolir.gt')

print(p) # (Adrian Mann, wa@zolir.gt)

print(repr(p)) # Pair('Adrian Mann', 'wa@zolir.gt')
print('{!r} {}'.format(p, p))

# 特殊方法`__repr__`会返回实例的代码表示，通常可以用该方法返回的字符串文本重新创建实例
print(p == eval(repr(p))) # True

with open('./README.md', encoding='UTF-8') as f:
  print('%r'%f)

```

## 自定义字符串格式

通过定义`__format__`方法支持对象的自定义输出格式:

```py
from datetime import date

class Date:
  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

  def __format__(self, format_spec):
    format_spec = 'ymd' if format_spec == '' else format_spec

    formats = {
      'ymd':'{0.year}-{0.month:02}-{0.day:02}',
      'mdy':'{0.month:02}/{0.day:02}/{0.year}',
      'dmy':'{0.day:02}/{0.month:02}/{0.year}'
    }

    return formats[format_spec].format(self)

d = Date(2025, 3, 1)

print(format(d)) # 2025-03-01
print(format(d, 'dmy')) # 01/03/2025
print('{:mdy}'.format(d))  # 03/01/2025


d = date(1997, 2, 22)

print(format(d))
print(format(d, '%A, %B %d, %Y'))
print('{:%d %b %Y}'.format(d))

```

## 使对象支持上下文管理协议

通过实现`__enter__`和`__exit__`方法使对象兼容`with`语句:

```py
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial

class LazyConnection:
  def __init__(self, addr, sock_family=AF_INET, sock_type=SOCK_STREAM):
    self.addr = addr
    self.family = sock_family
    self.type = sock_type
    self.sock = None

  def __enter__(self):
    if self.sock is not None:
      raise RuntimeError('Already connected!')
    self.sock = socket(self.family, self.type)
    self.sock.connect(self.addr)
    return self.sock

  # 参数为异常类型、值和对挂起异常的追溯对象
  def __exit__(self, exc_ty, exc_val, tb):
    self.sock.close()
    self.sock = None
    
    # 返回True时，with语句块中的异常会被清理，且程序会继续执行with语句块之后的代码
    # return True

with LazyConnection(('httpbin.org', 80)) as conn:
  # raise RuntimeError('Unknown error!')

  conn.send(b'GET /get HTTP/1.1\r\n')
  conn.send(b'Host: httpbin.org\r\n')
  conn.send(b'\r\n')

  res = b''.join(iter(partial(conn.recv, 8192), b''))

  print(res.decode())

print('finally')

```

上下文管理器最常用在需要管理类似文件、网络连接和锁这类资源程序中，这些资源的关键点在于它们必须
显式地进行关闭或释放才能正确工作。

> [contextmanager](https://docs.python.org/3/library/contextlib.html)

## 在创建大量实例时节省内存

在类定义中增加`__slots__`属性来大量减少实例对内存的使用:

```py
class Date:
  __slots__ = ['year', 'month', 'day']

  def __init__(self, year, month, day):
    self.year = year
    self.month = month
    self.day = day

```

> 通常情况下，应该只针对在程序中被当做数据结构而频繁使用的类上采用`__slots__`技法

## 在类中封装名称

通过特定的命名规则约束数据和方法的用途:

- 任何以单下划线`_`开头的名称总是被认为只属于内部实现，包括模块名、顶层函数名等
- 以双下划线`__`开头的名称属于私有属性，且会导致名称重整的行为，避免通过继承而覆盖

```py
class DevServer:
  def __init__(self):
    self._address = ''
    self.__framework = 'flask'

  def _apply(self):
    pass

  def __render(self):
    pass

  def run_and_serve(self):
    pass

server = DevServer()

print(server.__dict__) # {'_address': '', '_DevServer__framework': 'flask'}
print(DevServer.__dict__)

```

当定义的变量名称和保留字产生冲突时，应该在名称最后加上一个单下划线以示区别:

```py
lambda_ = 2.0

```

## 创建受管理的属性

## 调用父类的方法

## 在子类中扩展属性

## 创建新类型的类或实例属性

## 使用惰性计算属性

## 简化数据结构的初始化

## 定义接口或抽象基类

使用`abc`模块定义抽象基类:

```py
from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
  @abstractmethod
  def read(self, max_bytes=-1):
    pass

  @abstractmethod
  def write(self, data):
    pass

class SocketStream(IStream):
  def read(self, max_bytes=-1):
    pass

  def write(self, data):
    pass


def serialize(obj, stream):
  if not isinstance(stream, IStream):
    raise TypeError('Expected an IStream')


serialize('', SocketStream())

```


## 实现数据模型或类型系统

## 实现自定义容器

## 委托属性访问

## 在类中定义多个构造函数

## 创建实例而不调用 init

## 使用混入扩展类

## 实现有状态对象或状态机

## 根据字符串名称调用对象的方法

```py
import math
from operator import methodcaller

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __repr__(self):
    return 'Point({!r}, {!r})'.format(self.x, self.y)

  def distance(self, other):
    return math.hypot(self.x-other.x, self.y-other.y)

p = Point(2, 3)

print(getattr(p, 'distance')(Point(0, 0)))
print(methodcaller('distance', Point(0, 0))(p))

points = [
  Point(6, 3),
  Point(8, 0),
  Point(2, 0),
  Point(2, 0),
  Point(10, 4),
]

print(sorted(points, key=methodcaller('distance', Point(0, 0))))

```

## 实现访问者模式

## 无递归实现访问者模式

## 管理循环数据结构中的内存

## 使类支持比较操作

使用`functools.total_ordering`装饰器让类实例支持所有的比较操作:

```py
from functools import total_ordering

class Room:
  def __init__(self, name, length, width):
    self.name = name
    self.length = length
    self.width = width
    self.square_feet = self.length * self.width

@total_ordering
class House:
  def __init__(self, name, style):
    self.name = name
    self.style = style
    self.rooms = []

  def add_room(self, room):
    self.rooms.append(room)

  @property
  def living_space_footage(self):
    return sum(r.square_feet for r in self.rooms)
  
  def __repr__(self):
    return '{!r}: {!r} square foot {!r}'.format(self.name, self.living_space_footage, self.style)
  
  def __eq__(self, other):
    return self.living_space_footage == other.living_space_footage
  
  def __lt__(self, other):
    return self.living_space_footage < other.living_space_footage
  
h1 = House('h1', 'Cape')

h1.add_room(Room('Franklin Floyd', 13, 11))
h1.add_room(Room('Keith Coleman', 15, 25))
h1.add_room(Room('Mae Christensen', 19, 10))
h1.add_room(Room('Grace Doyle', 16, 21))

h2 = House('h2', 'Ranch')

h2.add_room(Room('Roy Kennedy', 20, 18))
h2.add_room(Room('Bobby Luna', 19, 22))
h2.add_room(Room('Effie Nash', 14, 16))

h3 = House('h3', 'Split')

h3.add_room(Room('Eunice Henry', 13, 22))
h3.add_room(Room('Gary Jones', 15, 11))
h3.add_room(Room('Grace Soto', 14, 10))
h3.add_room(Room('Steven Fitzgerald', 15, 13))

houses = [h1, h2, h3]

print([h.living_space_footage for h in houses])

print(h1 > h2) # True
print(h2 <= h3) # False
print(h2 >= h1) # False

print(max(houses)) # 'h1': 1044 square foot 'Cape'


```

## 创建缓存实例
