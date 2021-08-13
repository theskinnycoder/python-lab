'''
6a. Write a program to sort words in a file and put them in another file.The output file should have only lower case words, so any upper case words from source must be lowered (handle exceptions)
'''

file1 = input("Enter file name : ")
fopen = open(file1)
li = list()

for i in fopen:
    temp = i.split()
    for j in temp:
        li.append(j)
li.sort()
fopen.close()

file2 = open("tar.txt","w")

for i in li:
    file2.write(i)
    file2.write(" ")
file2.close()


'''
6b. Write a program return a list in which the duplicates are removed and the items are sorted from a given input list of strings.
'''

li = input("Enter list of strings : ").split()
s = set(li)
print(sorted(s))
