url = 'https://cn.bing.com/search?q=python&qs=ds&form=QBRE'

*_, hostname, _ = url.split('/')

print(hostname) 

def sum(items):
  head, *tail = items
  return head + sum(tail) if tail else head

print(sum(range(101)))
