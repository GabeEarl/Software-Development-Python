class Vehicle: # parent class for all vehicle
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type # vehicle type constructor

class Automobile(Vehicle): # subclass of vehicle that is an automobile with accompanying attributes
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type) # super method to call the parent class, vehicle for the vehicle type
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

vehicle_type: str = input('Enter the type of vehicle: ') # all the inputs for the user to input info that will be 
year: int = input('Enter the vehicle\'s year: ') #compiled into an object below called car that will be in the Automobile class
make: str = input('Enter the vehicle\'s make: ')
model: str = input('Enter the vehicle\'s model: ')
doors: int = input('Enter the amount of doors on the vehicle: ')
roof: str = input('Enter the type of roof the vehicle has: ')

car = Automobile(vehicle_type, year, make, model, doors, roof) # class inputing all the users inputs into Automobile class

print('The vehicle type is: ' + car.vehicle_type) # printing all the car classes attributes
print('The vehicle\'s year is: ' + car.year)
print('The vehicle\'s make is: ' + car.make)
print('The vehicle\'s model is: ' + car.model)
print('The vehicle\'s door count is: ' + car.doors)
print('The vehicle\'s roof is a: ' + car.roof)
