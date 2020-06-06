'''

Inheritance in Python
operator overloading -> 

    __add__(self, other)
    __sub__(self, other)
    __mul__(self, other)
    __mod__(self, other)

Function Overriding ->
    Happen in same way of like in C++

Order of constructor execution is user dependent not like in C++



'''
class C:
    def __init__(self):
        print("In C constructor")

#Parent Class
class A:
    def __init__(self, address):
        print("In parent class initializer")
        self.address = address
    
    @staticmethod
    def about():
        s = "Hey I am your parent class. You can access all the properties from me"
        print(s)

class B(A,C):
    def __init__(self, name, address):
        super().__init__(address)
        C.__init__(self)
        print("In child class initializer")
        self.name = name

b = B("Rahul", "A10/156")
A.about()
