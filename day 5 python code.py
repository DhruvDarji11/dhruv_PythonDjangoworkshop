#oop concept in python

"""
# 1st example
# CLASS AND ITS METHOD

class Myclass():

    def func1(self):
        print("Hello")

    def func2(self,name):
        print("Hello,",name)

myc=Myclass()   #object creation

myc.func1()
myc.func2("Dhruv Darji")
"""
"""
#2nd example
# Sum of 2 nos using class

class addition_of_2():
    
    def fun1(self,n1,n2):
        ans=n1+n2
        print("Sum of 2 nos is ",ans)


add2=addition_of_2()                               #OBJECT CREATION OF CLASS "addition_of_2"

add2.fun1(10,20)                                   #FUNCTON CALL
"""
"""
# 3rd example
#Default Constructor example

class MyClass:

    def __init__(self):                      #Defining default constuctor
        print('Hello World!!')

my=MyClass()
"""
"""
#4th example
#PARAMETERIZED CONSTRUCTOR

class Myclass:
    def __init__(self,name):    # constructor defination
        print("Name is:",name)

my=Myclass("Darji Dhruv")
"""
"""
#5th example
#ASSIGNING STRING VALUE TO CLASS VARIABLE

class Myclass:
    name=""                 #DEFINING CLASS VARIABLE

    def fun1(self):
        print("Hello,Welocome to python")

    def fun2(self,name):
        self.name=name            # here the input name is assigned to class variable

    def fun3(self):
        print("Hiiii,",self.name)

my=Myclass()
my.fun1()
my.fun2("Darji Dhruv")
my.fun3()
"""
"""
#6th example
#ASSIGNING STRING VALUE TO CLASS VARIABLE USING CONSTRUCTOR

class MyClass:
    name = ""

    def __init__(self,name):
        self.name=name

    def fun1(self):
        print("Name is :",self.name)

myc=MyClass("Darji Dhruv")
myc.fun1()
"""
"""
#7th example
#Assign string value to class variable using constructor
#Example for addition of 2 nos

class MyClass:
    n1 = ""
    n2 = ""

    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def funct1(self):
        ans=self.n1 + self.n2
        print("Sum of 2 nos is :",ans)

my=MyClass(10,15)
my.funct1()
"""

#INHERITANCE
"""
#8TH EXAMPLE
# SINGLE LEVEL INHERITANCE

class parent:

    def __init__(self):
        print("parent class constructor")

    def parentmethod(self):
        print("parent method is called")

class child(parent):

    def __init__(self):
        print("child class constructor is called")

    def childmethod(self):
        print("child method is called")

c=child()
c.childmethod()
c.parentmethod()
"""

"""
#MULTILEVEL INHERITANCE
#9TH EG
class grandfather:
    def __init__(self):
        print("calling grandfather constructor")
    def gramdfathermethod(self):
        print("calling grandfather method")

class father(grandfather):
    def __init__(self):
        print("calling father contructor")
    def fathermethod(self):
        print("calling father method")

class child(father):
    def __init__(self):
        print("calling child constructor")
    def childmethod(self):
        print("calling child methog")

c=child()
c.childmethod()
c.fathermethod()
c.gramdfathermethod()
"""
"""
#MULTIPLE INHERITENCE
#10TH EXAMPLE

class parent1:
    def __init__(self):
        print("constructor of parent1 is called")
    def parent1method(self):
        print("Method for parent1 is called")

class parent2:
    def __init__(self):
        print("Constructor for parent 2 is called")
    def parent2method(self):
        print("Method for parent 2 is called")

class child(parent1,parent2):
    def __init__(self):
        print("Constructor for child is called")
    def childmethod(self):
        print("Child method is called")

c= child()
c.childmethod()
c.parent1method()
c.parent2method()
"""

"""
#11th example
#Hierarchical Inheritance

class parent:
    def __init__(self):
        print("Constructor of parent is called")
    def parentmethod(self):
        print("Method for parent is called")

class child1(parent):
    def __init__(self):
        print("constructor for child 1 is called ")
    def child1method(self):
        print("method for child 1 is called")

class child2(parent):
    def __init__(self):
        print("constructor for child 2 is called")
    def child2method(self):
        print("child2 method is called")

c1=child1()
c2=child2()
c1.child1method()
c2.child2method()
c1.parentmethod()
c2.parentmethod()
"""
"""
#hybrid inheritance
#12th example

class parent1:
    def parent1method(self):
        print("parent 1 method is called")

class parent2:
    def parent2method(self):
        print("parent 2 metjod is called")

class child1(parent1,parent2):
    def child1method(self):
        print("child 1 is of multiple inheritance and its method is called")

class child2(parent1):
    def child2method(self):
        print("child 2 is of single level inheritance and its method is called")

c1=child1()
c2=child2()
c1.child1method()
c2.child2method()
"""
"""
#13th example
#method overriding

class parent1:
    def function1(self):
        print("method for parent is called")

class child1:
    def function1(self):
        print("method for child is called")

c=child1()
p=parent1()
c.function1()
p.function1()
"""
#example 14
#METHOD OVERLOADING
class sumof:
    def addition(self,n1,n2):
        ans=n1+n2
        print("sum is :",ans)

    def addition(self,n1,n2,n3):
        ans=n1+n2+n3
        print("sum is:",ans)

s=sumof()
s.addition(10,10,10)




