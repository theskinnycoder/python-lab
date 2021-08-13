'''
1c. Write a program to get the binary form of a given number
'''

def get_binary(num):
    binary_str = ''
    while num > 0:
        a = num % 2
        num //= 2
        binary_str = f'{a}{binary_str}'
    return binary_str

num = int(input('Enter any number : '))

# Using bin()
print(f'The binary equivalent of {num} using bin() is : {bin(num)}')

# Without using bin()
print(f'The binary equivalent of {num} using custom function is : {get_binary(num)}')