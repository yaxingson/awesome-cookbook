# 目录

## 读取和写入 CSV 数据

用`csv`库处理CSV格式的数据文件:

```py
import csv
from collections import namedtuple

with open('./external/employees.csv') as f:
  f_csv = csv.reader(f)
  
  headers = next(f_csv)
  Row = namedtuple('Row', headers)

  for record in f_csv:
    row = Row(*record)
    print(row)

with open('./external/employees.csv') as f:
  f_csv = csv.DictReader(f)

  for row in f_csv:
    print(row)


headers = ['Model', 'Company', 'Public']
rows = [
  ('gpt-4-mimi', 'openai', False),
  ('llama', 'meta', True),
  ('gemini', 'google', False),
]

with open('./external/llms.csv', 'w') as f:
  f_csv = csv.writer(f)

  f_csv.writerow(headers)
  f_csv.writerows(rows)

```

> CSV编码规则

读取以`;`键分隔的数据:

```py
import csv
import re
from collections import namedtuple

col_types = [str, str, float, int, str]

with open('./external/packages.csv') as f:
  f_csv = csv.reader(f, delimiter=';')

  headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
  Row = namedtuple('Row', headers)

  for record in f_csv:
    record = [convert(value) for convert, value in zip(col_types, record)]
    row = Row(*record)
    print(row)

```

> [pandas](http://pandas.pydata.org)

## 读取和写入 JSON 数据

编码和解码JSON格式的数据:

```py
import json
import pickle

config = {
  "server":{
    "host":"127.0.0.1",
    "open":True
  },
  'database':{
    "port":3306
  }
}

json_str = json.dumps(config)

print(json.loads(json_str))

```

读写以JSON格式编码的数据文件:

```py
import json

settings = {
  'test':{
    'globals':True,
    'server':{
      'host':'127.0.0.1',
      'port':3306
    }
  }
}

with open('./external/settings.json', 'w') as f:
  json.dump(settings, f)

with open('./external/package.json') as f:
  pkg = json.load(f)
  print(pkg['description'])

```




## 解析简单的 XML 数据

```py
from xml.etree.ElementTree import parse
from lxml.etree import parse as xml_parse

with open('./external/feed.xml', encoding='utf-8') as f:
  doc = parse(f)
  
  for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title.strip())
    print(date)
    print(link)
    print()

  desc = doc.find('channel/description')


  print(desc.tag)
  print(desc.text)
  print(desc.get('lang'))

```

## 逐步解析巨大的 XML 文件

## 将字典转换为 XML

利用`xml.etree.ElementTree`库创建XML文档:

```py
from xml.etree.ElementTree import Element, tostring
from xml.sax.saxutils import escape, unescape

def dict_to_xml(tag, d):
  elem = Element(tag)
  for key, val in d.items():
    child = Element(key)
    child.text = str(val)
    elem.append(child if not isinstance(val, dict) else dict_to_xml(key, val))
  return elem

def dict_to_xml_str(tag, d):
  parts = [f'<{tag}>']
  for key, val in d.items():
    val = val if not isinstance(val, str) else escape(val)
    parts.append(f'<{key}>{val}</{key}>' if not isinstance(val, dict) 
                 else dict_to_xml_str(key, val))
  return ''.join(parts)

pkg = {
  'author':'yaxingson, <3228891558@qq.com>',
  'version':'0.0.1',
  'private':True,
  'repository':{
    'type':'git',
    'url':'https://github.com/yaxingson/estdlib.git'
  }
}

el = dict_to_xml('package', pkg)

print(el)
print(tostring(el).decode())

print(dict_to_xml_str('package', pkg))

```

## 解析、修改和重写 XML



## 解析带命名空间的 XML 文档




## 与关系数据库交互

在Python中，表达数据库表中的行数据的标准方式是采用元组序列:

```py
import sqlite3
from pathlib import Path
from datetime import datetime
from decimal import Decimal

file_path = Path('./external/test.db')

if file_path.exists():
  file_path.unlink()

def adapt_datetime(datetime):
  return datetime.isoformat()

def adapt_decimal(decimal):
  return str(decimal)

sqlite3.register_adapter(datetime, adapt_datetime)
sqlite3.register_adapter(Decimal, adapt_decimal)

employees = [
  ('Rachel Austin', 35, 3.7, Decimal('4438.65'), datetime(2012, 3, 22)),
  ('Marion Wagner', 31, 6.1, Decimal('4451.20'), datetime(2020, 7, 23)),
  ('Jesus Jensen', 34, 4.9, Decimal('7159.88'), datetime(2007, 6, 27)),
  ('Mamie Hill', 27, 2.6, Decimal('4211.20'), datetime(2002, 9, 26)),
  ('Essie Garza', 30, 8.9, Decimal('7166.43'), datetime(2012, 2, 24)),
]

create_sql = '''
CREATE TABLE employees (
  name TEXT,
  age INTEGER,
  performance REAL,
  salary REAL,
  entry_date TEXT
)
'''

insert_sql = '''
INSERT INTO employees VALUES (?,?,?,?,?)
'''

select_sql = '''
SELECT * FROM employees WHERE performance >= ?
'''

# 连接数据库
db = sqlite3.connect(
  database='./external/test.db'
)

# 创建游标，并执行SQL查询
cur = db.cursor()

cur.execute(create_sql)
cur.executemany(insert_sql, employees)

db.commit()

for row in cur.execute(select_sql, (5.0,)):
  print(row)

```

> 为了防止SQL注入攻击，应避免用Python的字符串格式化操作（`%`或`format`方法）创建组成SQL语句的字符串

## 解码和编码十六进制数字

编码和解码由十六进制数组成的字节串:

```py
import binascii
import base64

with open('./external/logo.png', 'rb') as f:
  data = f.read()
  print(binascii.b2a_hex(data))
  print(base64.b16encode(data))

```

## 解码和编码 Base64

采用`Base64`编码对二进制数据进行编码和解码:

```py
import base64

with open('./external/logo.png', 'rb') as f:
  data = base64.b64encode(f.read()).decode("ascii")
  print(f'data:image/png;base64,{data}')

```

> Base64只能用于面向字节的数据上，例如字节串、字节数组等

## 读取和写入结构的二进制数组

## 读取嵌套和可变大小的二进制结构

## 数据汇总和统计分析

使用`Pandas`库实现数据统计和分析:

```py
import pandas

followers = pandas.read_csv('./external/followers.csv', skipfooter=0, engine='python')

print(followers)
print(followers['login'].unique())
print(followers[followers['id'] <= 10**8])
print(followers['login'].value_counts()[:5])

```
