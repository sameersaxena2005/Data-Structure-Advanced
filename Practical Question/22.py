# 22. Write a code that takes a dictionary as input and returns a sorted version based on values
d = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_dict)
