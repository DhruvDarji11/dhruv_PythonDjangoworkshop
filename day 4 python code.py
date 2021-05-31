"""
# 1st function

def my_function():
    print("Hello World!!")

my_function()
"""
"""
#2nd function
#example of function with argument

def my_function(name):
    print("Hello ",name)

my_function("dhruv")
"""
"""
#3rd funtion example
#function with return type

def my_function(name):
    return name

na=my_function("Dhruv, how are you")
print(na)
"""
"""
#4th function example
#multiple return Statement

def my_function():
    name="Dhruv"
    surname="Darji"
    return name,surname

name,surname=my_function()
print("Name:",name)
print("Surname:",surname)
"""
"""
#5th function eg
#Python default argument

def sumof(a=5,b=10):
    print("sum of 2 nos is :",a+b)

sumof(10,20)
sumof()                  #HERE DEFAULT VALUE IS TAKEN WHICH WE HAVE PROVIDED
"""
"""
#6th funuction example
#Python key word ARGUMENT

def sumof(a,b):
    print("sum of 2 os is:",a+b)
sumof(b=10,a=12)
"""
"""
#7th function eg
#Python VARIABLE LENGTH ARGUMENT

def add(*num):
    sum=0

    for n in num:
        sum=sum+n
    print("sum is :",sum)

add(10,20)
add(20,30,40)
"""

"""
#8th function
# VARIABLE LENGTH: KEY WORD ARGUMENT

def my_fun(**arg):
    for i,j in arg.items():
        print(i,j)

my_fun(Name="Dhruv",Surname="Darji")
"""

"""
#9TH FUNCTION
#SCOPE OF VARIABLE

def my_function():
    x=10
    print(x)

x=100
my_function()    #calling function so local variable will be called
print(x)         #HERE "GLOBAL" VARIABLE WILL BE CALLED
"""
"""
#10TH FUNCTION
#INDENTATION IS MUST IF WE DON'T THEN IT WILL CALL AN ERROR "INDENTATION ERROR"

def my_function():
print("Hello World!!")

my_function()
"""
"""
#11TH FUNCTION
#import module form another module

import demo
name=demo.my_function("Dhruv Darji")
print(name)
"""

"""
#OPERATORS IN PYTHON
#ARITHMETIC OPERATOR
x=10
y=9
print("x+y",x+y)
print("x-y",x-y)
print("x*y",x*y)
print("x/y",x/y)
print("x//y",x//y)
print("x^y",x**y)
"""
"""
#COMPARISION OPERATOR   <, >,==,!=,>=,<=

x,y=10,5
print("x>y",x>y)

#LOGICAL OPERATOR                 and,or,not are logical operator
#Example of and

x,y,z=10,9,8

if x>y and x>z:
    print("x is max")
elif y>x and y>z:
    print("y is max")
else:
    print("z is max")
"""
"""
#ASSIGNMENT OPERATOR
#USED TO ASSIGN A VALUE TO A VARIABLE LOCATING TO A SPECIFIC ADDRESS IN MEMORY

# THEY ARE =,+=,-=,*=,/=,%=,//=,**=

X=10
print(X)
X +=10
print(X)
"""
"""
#MEMBERSHIP OPERATOR
#IN , NOT IN ARE MEMBERSHIP OPERATOR
#OP IN TRUE OR FALSE

x=10
l1=[10,20,30]
print(x in l1)
"""
"""
#IDENTITY OPERATOR
#IT IS USED TO CHECK WHETHER OPERATORS ARE SAME OR NOT
# IS ,IS NOT ARE IDENTITY OPERATOR

X=10
y=10
print(X is y)
"""


















