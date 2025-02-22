from collections import Counter

word_list = [
  "dog", "banana", "cat", "dog", "elephant", "flower", 
  "guitar", "happiness", "island", "flower", "kite", "lion",
  "dog", "banana", "island", "dog", "apple", "island", "cat"
]

word_count = Counter(word_list)
top_three = word_count.most_common(3)

print(word_count)
print(top_three)

more_words = ['cat', 'dog', 'lion']

# word_count.update(more_words)

for word in more_words:
  word_count[word] += 1

print(word_count['dog'])

a = Counter(['green', 'blue', 'red', 'blue', 'blue'])
b = Counter(['blue', 'pink', 'orange'])

c = a + b

print(c)

d = a - b 

print(d)
