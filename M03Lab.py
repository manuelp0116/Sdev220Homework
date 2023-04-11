'''
Manuel Paredes
M03 Lab- case study: list, Functions, and classes
this app will organize the input of the user related to the vehicle, in this version of the application its just
the car object, but It could be expanded to allow us to get all kinds of vehicles, and make it more dinamic, 
'''

class vehicle(): #super class
    def __init__(self,Type):
        self.type = type
        pass
    

class automobile(vehicle): #child class, Inherits type
    def __init__(self, Type, year, make, model, doors, roof):
        super().__init__(Type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
        
        
#get user input
vehicleType = input("Enter the vehicle type: ")
vehicleYear = input("Enter vehicle year: ")
vehicleMake = input("Enter vehicle make: ")
vehicleModel = input("Enter vehicle model: ")
vehicleDoors = input("Enter the number of doors (2 or 4) : ") 
vehicleRoof = input("Enter vehicle roof (solid or sun roof): ") 

#create the car object, and use the vehicle class for the attributes.
car = automobile(vehicleType, vehicleYear, vehicleMake, vehicleModel, vehicleDoors, vehicleRoof)

#print all the attributes in an organized manner
print('Vehicle type:', car.type)
print('Year:', car.year)
print('Make:', car.make)
print('Model:', car.model)
print('Number of doors:', car.doors)
print('Type of roof:', car.roof)