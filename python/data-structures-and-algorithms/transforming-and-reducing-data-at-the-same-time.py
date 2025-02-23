import os

numbers = [1, 2, 3, 4, 5]
s = sum(x * x for x in numbers)

print(s)

s = ('ACME', 50, 123.45)

print(','.join(str(x) for x in s))

portfolio = [
  {'name':'APPLE', 'shares': 34},
  {'name':'META', 'shares': 80},
  {'name':'SOFTBANK', 'shares': 29},
  {'name':'IBM', 'shares': 41},
  {'name':'GOOGLE', 'shares': 59},
]

print(min(s['shares'] for s in portfolio))

files = os.listdir('.')

print(files)

if any(name.endswith('.py') for name in files):
  print('There be python!')
else:
  print('Sorry, no python.')

