# 15. Implement a code to find and remove duplicates from a list while preserving the original order
lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for num in lst:
    if num not in unique_list:
        unique_list.append(num)

print(unique_list)
