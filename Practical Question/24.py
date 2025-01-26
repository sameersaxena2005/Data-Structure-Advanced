# 24. Write a code that takes a list of words as input and returns a dictionary
#     where the keys are unique words and the values are their frequencies
words = ["apple", "banana", "apple", "orange", "banana", "banana"]
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
