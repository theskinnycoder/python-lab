'''
2b. Write a program to check whether a given number has even number of 1's in its binary
representation (No control flow, the number can be in any base)
'''

def has_even_number_of_1s(num):
    count = bin(num).count('1')
    return (not (count % 2)), count

num = int(input('Enter any decimal number : '))
binary_equivalent = bin(num)

has_even_1s, num_of_1s = has_even_number_of_1s(num)

print(f"The binary equivalent of {num} has {'even' if has_even_1s else 'odd'}({num_of_1s}) number of 1s")
