prices = {
  'APPLE': 261.28,
  'IBM': 203.74,
  'GOOGLE': 384.15,
  'SOFTBANK': 133.72,
  'DROPBOX': 58.51,
}

p1 = { key:value for key, value in prices.items() if value > 300 }

print(p1)

tech_names = {'APPLE', 'GOOGLE', 'DROPBOX'}

p2 = { key:value for key, value in prices.items() if key in tech_names }

print(p2)
