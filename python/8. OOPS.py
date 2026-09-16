class Car:
    total_cars=0   #class variable, shared by all objects of class

    def __init__(self,brand,model): #constructor, self is link between class and object
        self.__brand=brand  # __ means private variable
        self.__model=model
        Car.total_cars+=1   #incrementing class variable

    def fullname(self): #function
        return f"{self.__brand} {self.__model}"

    def get_brand(self):    #gets/reads private variable
        return self.__brand +"!"
    
    def set_brand(self,brand):    #changes/updates private variable
        self.__brand=brand

    def Fuel_Type(self):   #Polymorphism
        return "Petrol or Diesel"

    @staticmethod   #decorator, static method can be called without creating object
    def car_type():
        return "Car"

    @property   #decorator, getter method, no overwriting, read-only 
    def model(self):
        return self.__model

    
class ElectricCar(Car): #Inheritance
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)   #used to inherit as they were used earlier
        self.battery_size=battery_size

    def Fuel_Type(self):   #Polymorphism
            return "Electric Charge"


my_car=Car("Hyundai","Creta") #object
# print(my_car.__brand) wont work as private variable. use getter.
print(my_car.model)#use of decorator
# my_car.model="Verna" will not work.
print(f"Total cars created: {Car.total_cars}")
print(my_car.fullname())
print(my_car.get_brand())
my_car.set_brand("Toyota")
print(my_car.get_brand())   # Toyota
print(my_car.fullname())    # Toyota Creta

my_tesla=ElectricCar("Tesla","Model S","85KWh")
print(my_tesla.model, '-', my_tesla.battery_size)
print(my_tesla.fullname())

print(my_car.Fuel_Type())
print(my_tesla.Fuel_Type())

print(Car.car_type()) 

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar)) #used to check if obj is instance of class or not.



class Battery:
    def Battery_info(self):
        return "Battery class"

class Engine:
    def Engine_info(self):
            return "Engine class"

class ElectricCar2(Battery,Engine,Car):
    pass

my_new_Tesla=ElectricCar2("Tesla","Model-S")
print(my_new_Tesla.Battery_info())
print(my_new_Tesla.Engine_info())