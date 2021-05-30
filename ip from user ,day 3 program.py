
"""    #program 1
# Calculate average of 5 nos.
print("Enter 5 nos.")
sum=0
for i in range(0,5):
    n=int(input())
    sum=sum+n

avg=sum/5
print("avg of 5 nos is :",avg)
"""

"""
#program 2
#check whether the no is even or odd

print("Enter a number:")
n=int(input(""))
if n%2==0:
    print("number is even")

else:
    print("number is odd")
"""

"""
#program 3
#take a year and check whete it is leap year or not

year=int(input("Enter a year"))
if year%100==0:                                   #to check is it a centuary or not
    if year%400==0:               #if it is a centuary then to be as a leap year it should also be divisible by 400
        print(year,"is a leap year")
    else:
        print(year,"is a not leap year")
else:
    if year%4==0:
        print(year,"is a leap year")
    else:
        print(year,"is not a leap year")
"""
'''
#program 4
#check no is 0 , +ve or -ve

n=int(input("Enter a no:"))
if n>0:
    print(n,"is positive")
elif n<0:
    print(n,"is negative")
else:
    print("number is zero")
'''

"""
#program 5
#2 nos and print max no and check if it is similar


n1=int(input("Enter no:"))
n2=int(input("Enter no:"))
if n1>n2:
    print(n1,"is greatest")
elif n1==n2:
    print("both nos are same")
else:
    print(n2,"is greatest")

"""


"""
#program 6
#find factorial of that number

n=int(input("Enter a no:"))
ans=1
for i in range(1,n+1):
    ans=ans*i
print("Factorial of ",n,"is",ans)
"""
'''
#program 7
#swap 2 nos using 3 rd variable

n1=int(input("Enter 1st value:"))
n2=int(input("Enter 2nd value:"))

c=n1
n1=n2
n2=c
print("After swapping")
print("1st value is",n1)
print("2nd value is",n2)
'''
"""
#program 8
#2 nos and print smallest no


n1=int(input("Enter no:"))
n2=int(input("Enter no:"))
if n1>n2:
    print(n2,"is smallest")
elif n1==n2:
    print("both nos are same")
else:
    print(n1,"is smalltest")
"""

"""
#program 9
#find no is smaller than 100 then is it even or odd

n=int(input("Enter a no:"))
if n>100:
    print("no is greater than 100")
else:
    if n % 2 == 0:
        print("number is even")

    else:
        print("number is odd")
"""
"""
#program 10
#if no is less than 10 print its square

n=int(input("Enter a no:"))
if n<10:
    print("square is",n*n)
else:
    print("no is > than 10")

"""
"""
#program 11
#NESTED IF ELSE to check nos are equal, less than or greater than

n1=int(input("Enter no:"))

if n1>0:
    if n<
else:
"""
"""
#PROGRAM 12
#Find Greatest no form 3 no using if.. else ladder
n1=int(input("enter 1st no:"))
n2=int(input("Enter 2nd no:"))
n3=int(input("Enter 2nd no:"))

if n1>n2:
    if n1>n3:
        print(n1,"is max")
    else:
        print(n3,"is max")
else:
    if n2>n3:
        print(n2,"is max")
    else:
        print(n3,"is max")
        
"""
"""
#PROGRAM 13
#FIND smallest no from 3 nos usind logical operator

n1=int(input("enter 1st no:"))
n2=int(input("Enter 2nd no:"))
n3=int(input("Enter 2nd no:"))


if n1>n2 and n1>n3:
    print(n1,"is max")
elif n2>n3 and n2>n1:
    print(n2,"is max")
else:
    print(n3,"is max")
"""
"""
#PROGRAM 14
#SWAP 2 nos without using 3rd variable

n1=int(input("Enter 1st no:"))
n2=int(input("Enter 2nd no:"))

n1=n1+n2
n2=n1-n2
n1=n1-n2

print("After swapping")
print("n1 is",n1,"n2 is ",n2)
"""

#PROGRAM 15
#Starting no and ending no and print the series

s1=int(input("Enter starting no:"))
e1=int(input("Enter starting no:"))
n=s1
while n!=e1:
    print(n)
    n=n-3
print(e1)







