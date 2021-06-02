#DAY 5 ADVANCED TASK : WRITE PROGRAM

"""
#1ST EXAMPLE

class cal1:
    n1=""
    n2=""
    n3=""
    def setdata(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
        print(self.n1,"",self.n2,"",self.n3,"are inputed values")

    def display(self):
        ans=self.n1+self.n2+self.n3
        print("sum of 3 nos is ",ans)

s=cal1()
s.setdata(10,20,30)
s.display()
"""
"""
#2nd EXAMPLE

class cal2:
    r=""
    ans=""
    def setdata(self,r):
        self.r=r
        print("Inputed radius is",self.r)
    def area(self):
        self.ans=3.14*self.r*self.r

    def display(self):
        print("Area of circle is :",self.ans)

ar=cal2()
ar.setdata(10)
ar.area()
ar.display()
"""
"""
#3rd example

class cal3:
    p=""
    r=""
    t=""
    ans=""
    def __init__(self,p,r,t):
        self.p=p
        self.r=r
        self.t=t

        print("Principle amount is:",self.p,",Rate of inteest is:",self.r,",Time interval in years is:",self.t)

    def calInterest(self):
        self.ans=self.p*self.r*self.t/100

    def display(self):
        print("Simple Interest is :",self.ans)

a=cal3(1000,10,2)
a.calInterest()
a.display()
"""
"""
#4th example

class cal4:
    n=""
    ans=""
    def setdata(self,n):
        self.n=n

    def display(self):
        self.ans=self.n*self.n
        return self.ans

sq=cal4()
sq.setdata(11)
ans=sq.display()
print("Square is :",ans)
"""
"""
#5th Example

class employee:
    name=""
    designation=""

    def __init__(self,name,designation):
        self.name=name
        self.designation=designation
        print("Name is :",self.name," and Designation is:",self.designation)

    def details(self):
        print("name:",self.name)

class salary(employee):
    def __init__(self,salary):
        print("Salary is ",salary)

    def details(self,name,designation):
        self.name=name
        self.designation=designation
        print("Name is :",self.name," and Designation is:",self.designation)

e=employee("Dhruv","Django developer")
s=salary(100000)
s.details("Darji","web developer")
"""
"""
#Example 6
class cal6:
    length=""
    breadth=''
    ans=""

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        print("Inputted length ",self.length,"breadth is:",self.breadth)

    def calArea(self):
        self.ans=self.length*self.breadth

    def display(self):
        print("Area of Rectangle is:",self.ans)

a=cal6(10,20)
a.calArea()
a.display()
"""

"""
#7th example

class cal7:
    length=""
    ans=""

    def setdata(self,length):
        self.length=length
        print("Inputted length is:",self.length)

    def area(self):
        self.ans=self.length*self.length

    def display(self):
        print("Area of Square is:",self.ans)

a=cal7()
a.setdata(10)
a.area()
a.display()
"""
"""
#8th Example
class publisher:
    name=""
    page_no=""
    playing_time=""
    def details(self,name):
        self.name=name
        print("Name is :",self.name)

class book(publisher):
    def details(self,name,page_no):
        self.name=name
        self.page_no=page_no
        print("Name is:",self.name,"Number of page is:",self.page_no)

class tape(publisher):
    def details(self,name,playing_time):
        self.name=name
        self.playing_time=playing_time
        print("NAme is:",self.name,"Playing time of tape is:",self.playing_time,"in minute")

a=book()
b=tape()
a.details("Raja",120)
b.details("Ramu",120)
"""
"""
#9th example
class scheme:
    scheme_id=""
    scheme_name=""
    outgoing_rate=""
    message_charge=""

    def display(self,scheme_id,scheme_name,outgoing_rate,message_charge):
        self.scheme_id=scheme_id
        self.scheme_name=scheme_name
        self.outgoing_rate=outgoing_rate
        self.message_charge=message_charge

        print("Scheme id is",self.scheme_id)
        print("scheme name is:",self.scheme_name)
        print('outgoing rate is',self.outgoing_rate)
        print("message charge is",self.message_charge)
        print("")

class customer(scheme):
    cust_id=""
    cust_name=""
    mobile_no=""

    def display(self, scheme_id, scheme_name, outgoing_rate, message_charge,cust_id,cust_name,mobile_no):
        self.scheme_id = scheme_id
        self.scheme_name = scheme_name
        self.outgoing_rate = outgoing_rate
        self.message_charge = message_charge
        self.cust_id = cust_id
        self.cust_name = cust_name
        self.mobile_no = mobile_no

        print("Scheme id is", self.scheme_id)
        print("scheme name is:", self.scheme_name)
        print('outgoing rate is', self.outgoing_rate)
        print("message charge is", self.message_charge)
        print("customer id is :",self.cust_id)
        print("customer name is :",self.cust_name)
        print("customer mobile no is :",self.mobile_no)

c1=scheme()
c2=customer()
c1.display(12,"data pack","199 rs per month",1)
c2.display(13,"call","1 per minute",1,98,"Raja ram",9242424242)
"""

#10 th example
class arith:
    a=""
    b=""
    ans=""
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        self.ans=self.a+self.b
        return self.ans
    def subtract(self):
        self.ans=self.a-self.b
        return self.ans
    def multiply(self):
        self.ans=self.a*self.b
        return self.ans

z=arith(20,10)
a1=z.add()
a2=z.subtract()
a3=z.multiply()
print("Addition is:",a1)
print("subtration is:",a2)
print("multiplication is:",a3)









