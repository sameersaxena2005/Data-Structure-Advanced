# 25. Write a code that takes two dictionaries as input and merges them into a single dictionary. 
# If there are common keys, the values should be added together
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
merged_dict = dict1.copy()

for key, value in dict2.items():
    merged_dict[key] = merged_dict.get(key, 0) + value

print(merged_dict)
