# 35. Develop a code that prompts the user to input two sets of strings and prints their symmetric difference
set1 = set(input("Enter first set: ").split(","))
set2 = set(input("Enter second set: ").split(","))

print(set1 ^ set2)
