# 26. Write a code to access a value in a nested dictionary. If the key path does not exist, return None...
nested_dict = {"a": {"b": {"c": 10}}}
keys = ["a", "b", "c"]

value = nested_dict
for key in keys:
    value = value.get(key, None)
    if value is None:
        break

print(value)
