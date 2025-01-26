# 13. Create a code to count the occurrences of each element in a list and return a dictionary
lst = [1, 2, 2, 3, 3, 3, 4]
freq = {}

for num in lst:
    freq[num] = freq.get(num, 0) + 1

print(freq)
