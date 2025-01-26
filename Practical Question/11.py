# 11. Write a code to remove all occurrences of a specific element from a list
lst = [1, 2, 3, 2, 4, 2, 5]
element = 2

while element in lst:
    lst.remove(element)

print(lst)
