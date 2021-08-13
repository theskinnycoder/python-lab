'''
3a. Write a program to return the top 'n' most frequently occurring chars and their respective
counts. Ex: (aaaaaabbbbcccc, 2) should return [(a, 5), (b, 4)]
'''

def get_sorted_by_frequency(dic):
    return [(key, dic[key]) for key in sorted(dic.keys(), key=dic.get, reverse=True)]

def get_top_n_frequencies(chars_list, n):
    dic = {}
    for char in chars_list:
        dic[char] = chars_list.count(char)
    sorted_list = get_sorted_by_frequency(dic)
    return sorted_list[:n]


input_string = input('Enter any string : ')
num = int(input('Enter any number : '))

print(get_top_n_frequencies(list(input_string), num))