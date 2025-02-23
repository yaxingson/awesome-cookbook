from collections import namedtuple

User = namedtuple('User', ('name', 'email'))

user = User('Lilly Moss', 'rucasla@guha.ps')

print(issubclass(User, tuple)) # True

print(user) # User(name='Lilly Moss', email='rucasla@guha.ps')
print(user.email) # rucasla@guha.ps

print(len(user)) # 2

username, email = user

print(f'<{username},{email}>') # <Lilly Moss,rucasla@guha.ps>

# namedtuple是不可变的
try:
  user.name = 'Raymond Leonard'
except AttributeError:
  pass

user = user._replace(name='Raymond Leonard')

print(user.name) # Raymond Leonard

# 利用`_replace()`方法填充具有可选或缺失字段的命名元组
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

stock_proto = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
  return stock_proto._replace(**s)

d = {'name':'ACME', 'shares':100}

print(dict_to_stock(d)) # Stock(name='ACME', shares=100, price=0.0, date=None, time=None)
