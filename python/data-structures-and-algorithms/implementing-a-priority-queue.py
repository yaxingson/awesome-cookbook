import heapq

class PriorityQueue:
  def __init__(self):
    self.queue = []
    self.index = 0

  def push(self, item, priority):
    heapq.heappush(self.queue, (-priority, self.index, item))
    self.index += 1

  def pop(self):
    return heapq.heappop(self.queue)[-1]

class Item:
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return 'Item({!r})'.format(self.name)

q = PriorityQueue()

q.push(Item('apple'), 6)
q.push(Item('banana'), 1)
q.push(Item('grade'), 3)
q.push(Item('strawberry'), 5)
q.push(Item('watermelon'), 3)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
