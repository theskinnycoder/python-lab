'''
2c. Write a program to sort given list of strings in the order of their vowel counts
'''

def get_number_of_vowels(string):
    vowel_counts = {}
    for vowel in "aeiou":
        vowel_counts[vowel] = string.count(vowel)
    return sum(vowel_counts.values())

def get_sorted_by_vowel_count(dic):
    return [(key, dic[key]) for key in sorted(dic.keys(), key=dic.get)]


input_strings = input('Enter space seperated list of words : ').split()
dic = {}

for string in input_strings:
    dic[string] = get_number_of_vowels(string)
print(get_sorted_by_vowel_count(dic))