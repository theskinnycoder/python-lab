'''
6b. Write a program return a list in which the duplicates are removed and the items are sorted
from a given input list of strings
'''

list_of_words = input('Enter comma seperated words :\n').split()
unique_set = set(list_of_words)
print(sorted(unique_set))