import re

birth = '11/27/2012'

print(re.match(r'\d+/\d+/\d+', birth))

# 当需要针对同一种模式做多次匹配时，通常会将正则表达式预编译为模式对象
pattern = re.compile(r'\d+/\d+/\d+')

print(pattern.match(birth))
print(pattern.match('Nov 27, 2012'))

text = 'Today is 11/27/2015. PyCon starts 3/13/2013'

print(pattern.findall(text))
