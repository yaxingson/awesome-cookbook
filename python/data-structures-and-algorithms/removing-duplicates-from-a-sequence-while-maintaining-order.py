# 参数key的作用是将序列中的不可哈希对象转换为可哈希类型，便于检测重复项
def dedupe(items, key=None):
  seen = set()
  for item in items:
    val = item if key is None else key(item)
    if val not in seen:
      yield item
      seen.add(val)

a = [1, 5, 2, 1, 9, 1, 5, 10]

print(list(dedupe(a)))

a = [
  { 'x':1, 'y':2 },
  { 'x':1, 'y':3 },
  { 'x':1, 'y':2 },
  { 'x':2, 'y':4 },
]

print(list(dedupe(a, key=lambda item: (item['x'], item['y']))))
print(list(dedupe(a, key=lambda item: item['x'])))

a = [1, 5, 2, 1, 9, 1, 5, 10]

print(list(set(a)))
