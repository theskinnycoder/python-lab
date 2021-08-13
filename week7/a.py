'''
7a. Write a program to test whether given strings are anagrams are not
'''

def anagrams(str1, str2):
    str1 = list(str1.lower())
    str2 = list(str2.lower())
    str1.sort()
    str2.sort()
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    else:
        return True

str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")
if anagrams(str1, str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")