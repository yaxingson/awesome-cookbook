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

## 逐步解析巨大的 XML 文件

## 将字典转换为 XML

## 解析、修改和重写 XML

## 解析带命名空间的 XML 文档

## 与关系数据库交互

## 解码和编码十六进制数字

## 解码和编码 Base64

## 读取和写入结构的二进制数组

## 读取嵌套和可变大小的二进制结构

## 数据汇总和统计分析



