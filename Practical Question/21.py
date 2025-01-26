# 21. Write a code that takes two tuples as input and returns a new tuple containing elements that are common
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
common = tuple(x for x in t1 if x in t2)
print(common)
