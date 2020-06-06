'''
Program to count number of variables created
'''
'''
class method -> used for change the class variables
static methods -> used as a utility function

Diff b/w class and static method ->
class variable can change the state of the class but not the static one
'''
class Bird:
    #class variable
    instance_count = 0
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.ref_count()
    
    @classmethod
    def ref_count(cls):
        Bird.instance_count += 1
    
    @staticmethod 
    def get_total():
        print(Bird.instance_count)

if __name__ == '__main__':
    b1 = Bird("a", "red")
    b2 = Bird("b", "black")
    # b3 = Bird("c", "yellow")
    Bird.get_total()
    
