'''
1d. Write a program to convert base36 to octal
'''

def base_36_to_octal(num):
    # Convert to decimal
    decimal_equivalent = int(num, 36)
    return str(oct(decimal_equivalent))[2:]

num = input('Enter any base 36 number : ')
print(f'The octal equivalent of {num} is : {base_36_to_octal(num)}')