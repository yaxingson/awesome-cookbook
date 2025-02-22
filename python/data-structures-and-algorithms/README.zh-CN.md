# 目录

## 将序列解包为单独的变量

任何序列（或可迭代对象）都可以通过赋值操作分解为单独的变量，唯一要求是变量的总数和结构要与序列一致:

```py
data = ['Max Haynes', 50, 91.9, (1997, 2, 15)]

name, shares, price, date = data

print(name) # 'Max Haynes'
print(date) # (1997, 4, 15)

name, shares, price, (year, month, day) = data

print(month) # 2

a, b, c, d, e = 'grape'

print(c) # a

```

当元素的数量不匹配时，会抛出`ValueError`错误:

```py
try:
  x, y, z = (6, 8)
except ValueError as e:
  print(f'{type(e).__name__}: {e}')

```

通常可以用一个用不到的变量名（比如`_`或`ign`）作为某些丢弃值的名称:

```py
_, shares, price, _ = ['Jorge Atkins', 67, 78.9, (2012, 12, 21)]

print(price) # 78.9

```

## 从任意长度的可迭代对象中解包元素

Python的"*表达式"可以解决可迭代对象分解的值过多的问题:

```py
grades = [99, 62, 61, 100, 63, 90, 80]

first, *middle, last = grades

print(middle) # [62, 61, 100, 63, 90]

user_record = ('Earl Johnson', 'lukot@ni.au', '773-555-1212', '847-555-1212')

name, email, *phone_numbers = user_record

print(phone_numbers) # ['773-555-1212', '847-555-1212']

*trailing, current = [69.2, 77.3, 47.6, 13.9, 30.8, 75.1, 37.9]

print(trailing) # [69.2, 77.3, 47.6, 13.9, 30.8, 75.1]
print(current) # 37.9

url = 'https://cn.bing.com/search?q=python&qs=ds&form=QBRE'

*_, hostname, _ = url.split('/')

print(hostname) # 'cn.bing.com'

```

*式语法迭代一个变长的元组序列:

```py
shapes = [
  ('circle', 5), 
  ('rect', 80, 30), 
  ('circle', 10),
]

def create_circle(radius):
  pass

def create_rect(width, height):
  pass

for name, *args in shapes:
  if name == 'circle':
    create_circle(*args)
  elif name == 'rect':
    create_rect(*args)

```

利用*分解操作实现递归算法:

```py
def sum(items):
  head, *tail = items
  return head + sum(tail) if tail else head

```

## 保留最后 N 个项目

保存有限的历史记录:

```py
from collections import deque

def search(lines, pattern, history=5):
  prev_lines = deque(maxlen=history)  
  for line in lines:
    if pattern in line:
      yield line, prev_lines
    prev_lines.append(line)

with open('./external/the-zen-of-python.txt') as f:
  for line, prev_lines in search(f, 'than'):
    for prev_line in prev_lines:
      print(prev_line, end='')
    print(line, end='')
    print('-'*20)

```

利用`deque`可以创建固定长度或无界限的队列:

```py
q = deque(maxlen=3)

q.append(5)
q.append(1)
q.append(9)

print(q) # deque([5, 1, 9], maxlen=3)

q.append(2)
q.append(7)

print(q) # deque([9, 2, 7], maxlen=3)

q = deque()

q.append(67)
q.append(51)
q.append(12)

print(q) # deque([67, 51, 12])

q.appendleft(34)

print(q) # deque([34, 67, 51, 12])

print(q.pop()) # 12
print(q) # deque([34, 67, 51])

print(q.popleft()) # 34
print(q) # deque([67, 51])

```

## 查找最大的或最小的 N 个项目

在某个集合中找出最大或最小的N个元素:

```py
import heapq

portfolio = [
  {'name':'IBM', 'shares': 51, 'price':72.93},
  {'name':'APPLE', 'shares': 65, 'price':448.81},
  {'name':'AliBABA', 'shares': 86, 'price':101.73},
  {'name':'FB', 'shares': 116, 'price':182.65},
  {'name':'AWS', 'shares': 45, 'price':348.72},
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])

print(cheap)
print(expensive)

```

当查找的最大或最小元素个数同集合中元素的总数目相比很小时:

```py
import heapq

numbers = [50, 23, -1, 52, 5, 46, 16, -6, 7, 20]

heapq.heapify(numbers)

print(numbers) # [-6, 5, -1, 7, 20, 46, 16, 52, 23, 50]

print(heapq.heappop(numbers)) # -6
print(heapq.heappop(numbers)) # -1
print(heapq.heappop(numbers)) # 5

```

> 查找集合中最大或最小的元素时, 内置函数`max`和`min`可以提供更好的性能

## 实现优先队列

利用heapq模块实现简单的优先级队列:

```py
import heapq

class PriorityQueue:
  def __init__(self):
    self.queue = []
    # 将具有相同优先级的元素以适当的顺序排列
    self.index = 0

  def push(self, item, priority):
    # priority取负值可以使队列能够按元素的优先级从高到低的顺序排列
    heapq.heappush(self.queue, (-priority, self.index, item))
    self.index += 1

  def pop(self):
    return heapq.heappop(self.queue)[-1]

class Item:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return 'Item({!r})'.format(self.name)

q = PriorityQueue()

q.push(Item('apple'), 6)
q.push(Item('banana'), 1)
q.push(Item('grade'), 3)
q.push(Item('strawberry'), 5)
q.push(Item('watermelon'), 3)

print(q.pop()) # Item('apple')
print(q.pop()) # Item('strawberry')
print(q.pop()) # Item('grade')
print(q.pop()) # Item('watermelon')
print(q.pop()) # Item('banana')

```

## 将键映射到字典中的多个值

利用`collections`模块中的`defaultdict`类创建一键多值字典:

```py
from collections import defaultdict

# 保留插入元素的顺序
d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d) # defaultdict(<class 'list'>, {'a': [1, 2], 'b': [4]})

# 消除重复元素且不关心插入元素的顺序
d = defaultdict(set)

d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d) # defaultdict(<class 'set'>, {'a': {1, 2}, 'b': {4}})

d = {}

d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print(d) # {'a': [1, 2], 'b': [4]}

```

## 保持字典的顺序

当对字典做迭代或序列化操作时，控制字典中元素的顺序:

```py
import json
from collections import OrderedDict

d = OrderedDict()

d['gpt'] = 1
d['deepseek'] = 2 
d['grok'] = 3
d['llama'] = 4
d['deepseek'] = 5

for key, value in d.items():
  print(f'({key}, {value})')

print(json.dumps(d))

```

## 使用字典进行计算

```py
prices = {
  'google': 45.16,
  'meta': 90.12,
  'dropbox': 37.10,
  'apple': 85.94,
  'softbank': 70.61
}

# `zip()`创建的迭代器只能被消费一次
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(min_price) # (37.1, 'dropbox')
print(max_price) # (90.12, 'meta')

# [(37.1, 'dropbox'), (45.16, 'google'), (70.61, 'softbank'), (85.94, 'apple'), (90.12, 'meta')]
print(prices_sorted) 

min_price_name = min(prices, key=lambda k:prices[k])
max_price_name = max(prices, key=lambda k:prices[k])

print(min_price_name)
print(max_price_name)

```

## 查找两个字典中的共同点

利用集合操作(并集、交集和差集)找出字典中的相同:

```py
a = { 'x':1, 'y':2, 'z':3 }
b = { 'w':10, 'x':11, 'y':2 }

print(a.keys() & b.keys()) # {'x', 'y'}
print(a.keys() - b.keys()) # {'z'}
print(a.items() & b.items())  # {('y', 2)}

c = {k:a[k] for k in a.keys() - {'z', 'w'}}

print(c) # {'x': 1, 'y': 2}

```

## 在保持顺序的同时从序列中删除重复项

## 命名切片

> 平面文件: 一种包含没有相对关系结构的记录文件

通过对切片命名避免硬编码的切片索引:

```py
url = 'https://cn.bing.com/search?q=dropbox&qs=n&form=QBRE&sp=-1&lq=0'

QUERY_SLICE = slice(url.index('?')+1, len(url))

query_string = url[QUERY_SLICE]

print(query_string) # q=dropbox&qs=n&form=QBRE&sp=-1&lq=0

print(QUERY_SLICE.start) # 27
print(QUERY_SLICE.stop) # 62
print(QUERY_SLICE.step)  # None

print(QUERY_SLICE.indices(len(url))) # (27, 62, 1)

```

## 确定序列中最常出现的项目

```py
from collections import Counter

word_list = [
  "dog", "banana", "cat", "dog", "elephant", "flower", 
  "guitar", "happiness", "island", "flower", "kite", "lion",
  "dog", "banana", "island", "dog", "apple", "island", "cat"
]

word_count = Counter(word_list)
top_three = word_count.most_common(3)

print(word_count)
print(top_three)

more_words = ['cat', 'dog', 'lion']

# word_count.update(more_words)

for word in more_words:
  word_count[word] += 1

print(word_count['dog'])

```

Counter对象支持各种数学运算:

```py
from collections import Counter

a = Counter(['green', 'blue', 'red', 'blue', 'blue'])
b = Counter(['blue', 'pink', 'orange'])

c = a + b

print(c)

d = a - b 

print(d)

```

## 按公共键对字典列表进行排序

## 对没有原生比较支持的对象进行排序

## 根据字段将记录分组

## 过滤序列元素

## 提取字典的子集

## 将名称映射到序列元素

## 同时转换和减少数据

## 将多个映射合并为单个映射
