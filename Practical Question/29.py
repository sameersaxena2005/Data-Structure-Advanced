# 29. Develop a code that prompts the user to input two sets of strings. Then, print the elements that are present in 
# the first set but not in the second set
set1 = set(input("Enter elements of first set: ").split(","))
set2 = set(input("Enter elements of second set: ").split(","))

print(set1 - set2)
