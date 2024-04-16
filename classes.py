# class

class Car:
    # constructor - method that runs
    def __init__(self, _color, _make):
        self._color = _color  # private
        self._make = _make

    # Getters - Accessors

    def get_color(self):
        return self._color
    
    def get_make(self):
        return self._make
    
    # Setters - Mutators

    def set_color(self, _color):
        # example: if the teach is the teacher of this course can change
        self._color = _color
        
    def run(self):
        print(f"{self._make} is running!! Vrroooom!!")

# Create an object of the class 'Car'
my_car = Car("White", "Honda")

print(my_car._color)
my_car.run()

your_car = Car("Black", "Toyota")
print(your_car._color)

your_car.run()

my_car._color = "Red"

class PetrolCar(Car):
    def __init__(self, _color, _make, capacity_of_tank):
        super().__init__(_color, _make)
        self.capacity_of_tank = capacity_of_tank

    def get_capacity(self):
        return self.capacity_of_tank
    
my_petrol_car = PetrolCar("Silver", "BMW", 50)
my_petrol_car.run()
print(my_petrol_car.get_capacity())

class ElectricCar(Car):
    
    # Overriding
    def run(self):
        print("I run silently!!")

my_electric_car = ElectricCar("Yellow", "Hyundai")
my_electric_car.run()


