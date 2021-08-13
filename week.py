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

def infinite_sequence(x):
    num = 0
    while i == x:
        yield num
        num += 1
        i+=1
gen = infinite_sequence(5)
print(next(gen))
