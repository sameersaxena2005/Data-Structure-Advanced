# 20. Write a code to shuffle a given list randomly without using built-in shuffle
import random

lst = [1, 2, 3, 4, 5]

for i in range(len(lst) - 1, 0, -1):
    j = random.randint(0, i)
    lst[i], lst[j] = lst[j], lst[i]

print(lst)
