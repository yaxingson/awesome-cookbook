from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
  {'name':'Hester Perez', 'country':'Moldova', 'birth':'07/24/2025'},
  {'name':'Olga Moss', 'country':'Germany', 'birth':'08/08/2025'},
  {'name':'Lelia Richardson', 'country':'Malawi', 'birth':'08/11/2025'},
  {'name':'Cecilia Guzman', 'country':'Panama', 'birth':'08/08/2025'},
  {'name':'Andrew Jimenez', 'country':'Jordan', 'birth':'08/08/2025'},
  {'name':'Leonard Carter', 'country':'Faroe Islands', 'birth':'03/15/2025'},
  {'name':'Lawrence Townsend', 'country':'Sierra Leone', 'birth':'03/13/2025'},
  {'name':'Louis Mitchell', 'country':'Niger', 'birth':'07/24/2025'},
]

rows.sort(key=itemgetter('birth'))

# `groupby`只能检查连续的项
for birth, items in groupby(rows, key=itemgetter('birth')):
  print(birth)
  for item in items:
    print(' ', item)

# 利用`defaultdict()`构建一键多值字典
rows_by_birth = defaultdict(list)

for row in rows:
  rows_by_birth[row['birth']].append(row)

print(rows_by_birth)
