# 7. a. Write a program to test whether given strings are anagrams are not

def Anagrams(str1,str2):
    str1=list(str1.lower())
    str2=list(str2.lower())
    str1.sort()
    str2.sort()
    for i in range(len(str1)):
        if str1[i]==str2[i]:
            continue
        else:
            return False
    else:
        return True

str1 = input("Enter string 1 : ")
str2 = input("Enter string 2 : ")
if(Anagrams(str1,str2)):
    print("The strings are Anagrams")
else:
    print("The strings are not Anagrams")


# 7. b. Write a program to implement left binary search.

def LBS(li,key):
    low = 0
    high = len(li) - 1
    l1=[]
    while low <= high:
        mid = (low + high) // 2
        if li[mid] > key:
            high = mid - 1
        elif li[mid] < key:
            low = mid + 1
        else:
            l1.append(mid)
            high = mid
            if low == high:
                return min(l1)
    return min(l1)

lis = list(map(int,input("Enter the list of numbers : ").split()))
k = int(input("Enter the number to be searched"))
print("The number found at index",LBS(lis,k))
