'''
8a. Write a class Person with attributes name, age, weight(kgs), height(ft) and takes them through the constructor and exposes a method get_bmi_result() which returns one of "underweight", "healthy", "obese"
'''

class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height * 0.305

    def get_bmi_result(self):
        bmi = self.weight / (self.height ** 2)
        if bmi >= 25:
            return "Obese"
        elif bmi >= 18.5 and bmi < 25:
            return "Healthy"
        else:
            return "UnderWeight"

name = input('Enter name : ')
age = int(input('Enter age : '))
weight = float(input('Enter weight in kg : '))
height = float(input('Enter height in feet : '))

p = Person(name, age, weight, height)
print(f'{p.name}, {p.age} is {p.get_bmi_result()}')