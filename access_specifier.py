'''Access Specifier in Python'''
class Student:
    _roll = None  #protected member
    __branch = None # private member
    name = None #public member
    
    def __init__(self, name, roll, branch):
        self.name = name
        self._roll = roll
        self.__branch = branch
        
    #private member function
    def __show_details(self):
        print(self.name)
        print(self._roll)
        print(self.__branch)
    
    #public member function
    def show_details(self):
        self.__show_details()
        
        
if __name__ == '__main__':
    s = Student("Rahul", "15028", "CSE")
    #public data member
    s.show_details()
