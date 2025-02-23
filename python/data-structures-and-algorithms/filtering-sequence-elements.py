from itertools import compress

grades = [82, 94, 70, 67, 66, 56, 74]

print([x for x in grades if x >= 80])

pass_grades = (x for x in grades if x >= 60)

for grade in pass_grades:
  print(grade)


def is_int(val):
  try:
    int(val)
    return True
  except ValueError:
    return False
  
values = ['1', '2', '-6', '-', '5', 'N/A', '0']

print(list(filter(is_int, values)))
print([v if is_int(v) else 0 for v in values])

countries = [
  'Greenland',
  'Cameroon',
  'Israel',
  'Cayman Islands',
  'United Arab Emirates',
  'Vietnam',
  'Nigeria',
]

selectors = [is_int(v) for v in values]
 
print(selectors)
print(list(compress(countries, selectors)))
