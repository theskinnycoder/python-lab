'''
7b. Write a program to implement left binary search
'''

def left_binary_search(lst, key):
    lst.sort()
    keys_list = []
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
            keys_list.append(mid)
    return min(keys_list)

lst = list(map(int, input("Enter the list of numbers : ").split()))
print()
key = int(input("Enter the number to be searched : "))
print("The number found at index : ", left_binary_search(lst, key))
