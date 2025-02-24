import re

text = 'year <= 2025'

NAME = r'(?P<NAME>[a-zA-Z_]\w*)'
NUM = r'(?P<NUM>\d+)'
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

correct_pattern = re.compile('|'.join([NAME, NUM, LE, LT, EQ, WS]))
incorrect_pattern = re.compile('|'.join([NAME, NUM, LT, LE, EQ, WS]))

scanner = correct_pattern.scanner(text)

for m in iter(scanner.match, None):
  print((m.lastgroup, m.group()))




