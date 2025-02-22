import heapq

numbers = [50, 23, -1, 52, 5, 46, 16, -6, 7, 20]

heapq.heapify(numbers)

print(numbers)

print(heapq.heappop(numbers))
print(heapq.heappop(numbers))
print(heapq.heappop(numbers))
