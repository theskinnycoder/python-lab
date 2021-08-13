'''
1a. Write a program to get the list of even numbers upto a given number.
'''

def get_list_of_evens(num):
    return [even_num for even_num in range(0, num, 2)]

num = int(input('Enter any number : '))
print(f'The list of evens upto {num} is : {get_list_of_evens(num)}')