# 27. Write a code that takes a dictionary as input and returns a sorted version of it based on 
# values (ascending or descending order)
d = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))  # Ascending order
print(sorted_dict)
