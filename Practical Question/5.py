# 5. Write a code to find all occurrences of a given substring within another string
main_str = "banana"
sub_str = "ana"
indices = []
i = main_str.find(sub_str)

while i != -1:
    indices.append(i)
    i = main_str.find(sub_str, i + 1)

print(indices)
