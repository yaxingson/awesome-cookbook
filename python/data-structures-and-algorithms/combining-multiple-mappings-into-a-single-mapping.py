from collections import ChainMap

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}

c = ChainMap(a, b)

print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))
print(list(c.keys()))

c['z'] = 10
c['w'] = 40
del c['x']

print(a)
print(b)

global_scope = ChainMap()
global_scope['x'] = 1

func_scope = global_scope.new_child()
func_scope['x'] = 2

block_scope = func_scope.new_child()
block_scope['x'] = 3

print(block_scope)
print(block_scope['x'])
print(block_scope.parents['x'])
print(block_scope.parents.parents['x'])
