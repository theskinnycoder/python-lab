'''
4a. Write a program to convert a given iterable into a list (Using iterator)
'''

iterator_1 = iter([5, 1, 4, 2, 3])
iterator_2 = iter({5, 1, 4, 2, 3})
print(list(iterator_1))
print(list(iterator_2))