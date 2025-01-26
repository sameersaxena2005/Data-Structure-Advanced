# 14. Write a code to reverse a list in-place without using any built-in reverse functions
lst = [1, 2, 3, 4, 5]
n = len(lst)

for i in range(n // 2):
    lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

print(lst)
