# 4. Write a code to check if two given strings are anagrams of each other
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print(True)
else:
    print(False)
