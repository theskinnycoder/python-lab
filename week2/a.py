'''
2a. Write a program to get the number of vowels in the input string (No control flow allowed)
'''

def get_number_of_vowels(string):
    vowel_counts = {}
    for vowel in "aeiou":
        vowel_counts[vowel] = string.count(vowel)
    return sum(vowel_counts.values())


input_string = input('Enter any string : ')
print(f'The number of vowels in {input_string} are : {get_number_of_vowels(input_string.lower())}')