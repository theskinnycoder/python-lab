'''
4d. Write a program to get a list of even numbers from a given list of numbers
'''

nums = list(map(int, input("Enter list of numbers : ").split()))

even_nums = [num for num in nums if num % 2 == 0]
print("The even numbers are : ", even_nums)