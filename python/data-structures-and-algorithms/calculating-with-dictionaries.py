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


