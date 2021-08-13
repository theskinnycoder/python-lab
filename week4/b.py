def square(x):
    return x ** 2

def custom_map(fun, li):
    temp = []
    it = iter(li)
    while True:
        try:
            temp.append(fun(next(it)))
        except StopIteration:
            return temp

val = custom_map(int, input("Enter the numbers : ").split())
print(val)
print("The square of the numbers is :", custom_map(square, val))