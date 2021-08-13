# 5. Write a program to implement round robin

from itertools import cycle, islice

def RR(*it):
    l = len(it)
    n = cycle(iter(i).__next__ for i in it)
    while l:
        try:
            for j in n:
                yield j()
        except StopIteration:
            l -= 1
            n = cycle(islice(n, l))

l1 = input("Enter list-1 : ").split()
l2 = input("Enter list-2 : ").split()
print(list(RR(l1,l2)))