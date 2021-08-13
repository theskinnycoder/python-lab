'''
4a. Write a program to convert a given iterable into a list. (Using iterator)
'''

val = iter(input("Enter the values : \n").split())
print("val is of Type :",type(val))
val2 = list(val)
print("val2 is of Type :",type(val2))


'''
4b. Write a program to implement user defined map() function
'''

def square(x):
    return x*x

def mapp(fun,li):
    temp = []
    it = iter(li)
    while True:
        try:
            temp.append(fun(next(it)))
        except StopIteration:
            return temp

val = mapp(int,input("Enter the numbers : ").split(" "))
print("The square of the Numbers is :",mapp(square,val))


'''
4c. Write a progra m to generate an infinite number of even numbers (Use generator)
'''

def evens():
    num = i = 0
    while True:
        yield num
        num += 2
        i+=1
gen = evens()
print(gen)
nu = 5
print("The first 5 even numbers are : ")
while nu:
    print(next(gen),end=" ")
    nu-=1


'''
4d. Write a program to get a list of even numbers from a given list of numbers.
'''

num = map(int,input("Enter list of numbers : ").split())
ev = [i for i in num if i%2==0 ]
print("The even number are :",ev)