# 6. Write a code to perform basic string compression using the counts of repeated characters
s = "aaabbccc"
compressed = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        compressed += s[i - 1] + str(count)
        count = 1

compressed += s[-1] + str(count)
print(compressed)
