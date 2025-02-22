try:
  x, y, z = (6, 8)
except ValueError as e:
  print(f'{type(e).__name__}: {e}')
