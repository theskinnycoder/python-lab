'''
1b. Write a program to get the ascii distance between two characters
'''

char_1 = input('Enter 1st character : ')
char_2 = input('Enter 2nd character : ')
distance = abs(ord(char_1) - ord(char_2))
print(f"The ASCII distance between '{char_1}' & '{char_2}' is : {distance}")