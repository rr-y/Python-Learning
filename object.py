#create Car Class
class Car:
    '''class variable'''
    car_type = "car"
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    #methods
    def get_details(self):
        print("Name of the car " + self.name + " price is "+self.price)
        
#create objects
#objects are created in the heap area
a = Car("Audi", "10k$")
b = Car("BMW", "20K$")

a.get_details()

        
