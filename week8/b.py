'''
8b. Write a program to convert the passed in positive integer number into its prime factorization form
'''

from math import sqrt

def get_prime_factorization_form(num):
    ans_list = []

    for factor in range(2, int(sqrt(num)) + 1):
        count = 0
        while num % factor == 0:
            count += 1
            num /= factor
        if count > 0:
            ans_list.append((int(factor), count))
    
    # If still any prime factor is left
    if num > 2:
        ans_list.append((int(num), 1))
    return ans_list

num = int(input('Enter any number : '))
print(f'The prime factorization form of {num} is : {get_prime_factorization_form(num)}')