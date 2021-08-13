'''
8.a. write a class Person with attributes name, age, weight (kgs), height (ft) and takes them through the constructor and exposes a method get_bmi_result() which returns one of "underweight", "healthy", "obese"
'''

class Person:
        def __init__(self,name,age,weight,height):
            self.name=name
            self.age=age
            self.weight=weight
            self.height=height
        def get_bmi_result(self):
            self.BMI = self.weight/((self.height*0.305)**2)
            if self.BMI<18.5:
                print("UnderWeight")
            elif self.BMI>18.5 and self.BMI<24.9:
                print("Healthy")
            else:
                print("Obse")
name=input()
age=int(input())
weight=float(input())
height=float(input())
p = Person(name,age,weight,height)
p.get_bmi_result()


'''
8.b. Write a program to convert the passed in positive integer number into its prime factorization form
'''

import math
def prime(n):
    c=0
    while n%2==0:
        c+=1
        n=n/2
    if c>0:
        print("("+"2"+","+str(c)+")",end="")
    for i in range(3,int(math.sqrt(n))+1,2):
        c1=0
        while n%i==0:
            n=n/i
            c1+=1
        if c1>0:
            print("("+str(i)+","+str(c1)+")",end="")
    if n>2:
        print("("+str(int(n))+","+"1"+")",)
n=int(input())
prime(n)

