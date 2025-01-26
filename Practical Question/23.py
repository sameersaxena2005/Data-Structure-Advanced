# 23. Write a code that inverts a dictionary (swap keys and values)
d = {'a': 1, 'b': 2, 'c': 1}
inverted = {}

for key, value in d.items():
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]

print(inverted)
