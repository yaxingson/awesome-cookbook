# 目录

## 编写接受任意数量参数的函数

可接受任意数量的位置参数的函数:

```py
def reduce(func, *args):
  print(args)

  result = args[0]
  for arg in args[1:]:
    result = func(result, arg)
  return result

print(reduce(lambda x,y: x+y, 1, 2, 3, 4, 5))

```

可接受任意数量的关键字参数的函数:

```py
import html

def make_element(name, value, **attrs):
  attr_list = [f' {item[0]}="{item[1]}"' for item in attrs.items()]
  attr_str = ''.join(attr_list)

  elem = '<{name}{attrs}>{value}</{name}>'.format(
    name=name,
    value=html.escape(value),
    attrs=attr_str
  )

  return elem

print(make_element('button', 'login', type='primary', size='large'))
print(make_element('pre', '<html></html>'))

```

> 在函数定义中，以"*"开头的参数只能作为最后一个位置参数，而以"**"开头的参数只能作为最后一个参数

在"*"开头的参数之后的函数参数称为`keyword-only`参数:

```py
def request(url, *_, method, query, headers):
  pass

```

## 编写仅接受关键字参数的函数

```py
def request(url, *, method='GET', query={}, headers={}):
  pass

help(request)

"""
Help on function request in module __main__:

request(url, *, method='GET', query={}, headers={})

"""

request('https://httpbin.org/get')
request('https://httpbin.org/get', query={
  'limit':5,
})

students = [
  {'name':'Isabel Berry', 'grade':66, 'height':1.84},
  {'name':'Edith Griffith', 'grade':60, 'height':1.77},
  {'name':'Fannie Williams', 'grade':100, 'height':1.88},
  {'name':'Daniel Dawson', 'grade':51, 'height':1.75},
  {'name':'Marion Parker', 'grade':60, 'height':1.72},
]

def mean(*args, key=None):
  if key is None:
    average = sum(args) / len(args)
  else:
    average = sum([key(item) for item in args]) / len(args)
  return round(average, 2)

print(mean(1, 2, 3, 4, 5))
print(mean(*students, key=lambda v:v['grade']))

```




## 将信息元数据附加到函数参数

函数的参数注解:

```py
def kebab_case(s:str) -> str:
  pass

print(kebab_case('camelCase')) # 'camel-case'
print(kebab_case('some whitespace')) # 'some-whitespace'
print(kebab_case('hyphen-text')) # 'hyphen-text'

help(kebab_case)

"""
Help on function kebab_case in module __main__:

kebab_case(s: str) -> str

"""

# 函数注解只会保存在函数的`__annotations__`属性中
print(kebab_case.__annotations__)

```

> Python解释器不会附加任何语法意义到函数参数的注解栅上，仅出现在帮助文档中，提高可读性

## 从函数返回多个值

```py
def calc(*values):
  return max(values), min(values)

print(calc(85.38, 53.94, 87.52, 33.47, 77.36, 69.29, 76.13))

# 通过逗号初始化元组
background_color = 255, 0, 0

print(background_color)

```

## 定义具有默认参数的函数

## 定义匿名或内联函数

定义仅仅完成表达式求值的内联函数:

```py
add = lambda x, y: x + y

print(add(7, 2))
print(add('hello', ' world'))

users = ["Myrtle Taylor", "Mable Sharp", "Madge Ortiz", "Bettie Matthews", "Vernon Patrick"]

print(sorted(users, key=lambda name: name.split()[-1].lower()))

```

> 微型函数

## 在匿名函数中捕获变量

## 使 N 参数可调用对象作为具有更少参数的可调用对象工作

## 用函数替换单方法类

通过**闭包**将只有单个方法的类转换为函数:

```py
from urllib.request import urlopen

class URLTemplate:
  def __init__(self, template):
    self.template = template
  
  def open(self, **kwargs):
    return urlopen(self.template.format_map(kwargs))

def url_template(template):
  def opener(**kwargs):
    return urlopen(template.format_map(kwargs))
  return opener

httpbin = url_template('https://httpbin.org/get?limit={limit}')

for line in httpbin(limit=5):
  print(line.decode('utf-8'))

```

> 当需要附加额外的状态给函数时，请考虑使用闭包

## 使用回调函数携带额外状态

## 内联回调函数

## 访问在闭包内定义的变量
