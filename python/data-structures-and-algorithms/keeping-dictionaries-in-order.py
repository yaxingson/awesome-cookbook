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
