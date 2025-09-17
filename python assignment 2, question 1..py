QUESTION 1.

class Vehicle:
     def _init_(self,brand,model):
         self.brand = brand
         self.model= model

class Car (Vehicle):
    def _init_(self,brand,model,num_doors):
        super()._init_(make,model)
        self.num_doors = num_doors

class Bike(Vehicle):
    def_init_(self,brand,model)
    super()._init_(make,model)
    self.bike_type = bike_type

    generic_vehicle = Vehicle('Generic','Vehicle')
    my_car = Car('Madza','Camry',4)
    my-bike == Bike('Trek','Marlin 5''Mountain')

    print(generic ,vehicle,describe)
    print(my_car.describe)
    print(my_bike.describe)

