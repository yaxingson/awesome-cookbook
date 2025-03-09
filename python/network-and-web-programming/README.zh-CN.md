# 目录

## 作为客户端与HTTP服务交互

以客户端的形式下载数据或同一个基于REST的API交互:

```py
from urllib import request, parse
from json import dumps, loads

# HTTP GET
url = 'https://httpbin.org/get'

params = {
  'kw':'python',
  'lang':'zh-cn'
}

querystring = parse.urlencode(params)

ret = request.urlopen(f'{url}?{querystring}')

response = ret.read()

print(response.decode())

# HTTP POST
DEEPSEEK_API_KEY = ''

url = 'https://api.deepseek.com/chat/completions'

headers = {
  'Content-Type':'application/json',
  'Authorization':f'Bearer {DEEPSEEK_API_KEY}'
}

body = {
  'model':'deepseek-chat',
  'messages':[
    {'role':'system', 'content':'You are a helpful assistant.'},
    {'role':'user', 'content':'python语言的主要特性有哪些'}
  ],
  'stream':False
}

data = dumps(body).encode('utf-8')

req = request.Request(url, data=data, headers=headers)

ret = request.urlopen(req)

response = loads(ret.read().decode('utf-8'))

print(response['choices'][0])

```

使用`requests`库:

```py
import requests

# HTTP POST
DEEPSEEK_API_KEY = 'sk-aa7c6321508c4804b9e42bbc1de4b778'

url = 'https://api.deepseek.com/chat/completions'

data = {
  'model':'deepseek-chat',
  'messages':[
    {'role':'user', 'content':'为什么天空是蓝色的'}
  ],
  'stream':False
}

headers = {
  'Content-Type':'application/json',
  'Authorization':f'Bearer {DEEPSEEK_API_KEY}'
}

res = requests.post(url, json=data, headers=headers)

print(res.text)
print(res.content)
print(res.json())

# HTTP HEAD
url = 'https://httpbin.org/head'

res = requests.head(url)

print(res.status_code)
print(res.headers)
print(res.cookies)

```


## 创建TCP服务器

## 创建UDP服务器

## 从CIDR地址生成IP地址范围

## 创建简单的基于REST的接口

## 使用XML-RPC实现简单的远程过程调用

## 解释器之间的简单通信

## 实现远程过程调用

## 简单地验证客户端

## 为网络服务添加SSL

## 在进程之间传递套接字文件描述符

## 理解事件驱动的I/O

## 发送和接收大型数组
