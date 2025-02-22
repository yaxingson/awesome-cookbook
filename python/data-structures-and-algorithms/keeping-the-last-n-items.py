from collections import deque

q = deque(maxlen=3)

q.append(5)
q.append(1)
q.append(9)

print(q)

q.append(2)
q.append(7)

print(q)

q = deque()

q.append(67)
q.append(51)
q.append(12)

print(q)

q.appendleft(34)

print(q)

print(q.pop())
print(q)

print(q.popleft())
print(q)
