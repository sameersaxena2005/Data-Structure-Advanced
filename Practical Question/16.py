# 16. Create a code to check if a given list is sorted (ascending or descending)
lst = [1, 2, 3, 4, 5]

if lst == sorted(lst):
    print("Ascending Order")
elif lst == sorted(lst, reverse=True):
    print("Descending Order")
else:
    print("Not Sorted")
