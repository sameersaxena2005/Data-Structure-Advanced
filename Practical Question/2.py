# 2. Write a code to count the number of vowels in a string
s = "hello world"
vowels = "aeiouAEIOU"
count = 0

for char in s:
    if char in vowels:
        count += 1

print(count)
