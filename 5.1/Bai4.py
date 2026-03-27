class Vehicle: 
  def __init__(self, brand, model, year): 
    self.brand = brand 
    self.model = model
    self.year = year 
  
  def display_info(self): 
    print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):
  def __init__(self, brand, model, year, num_doors): 
    super().__init__(brand, model, year) 
    self.num_doors = num_doors 

  def display_info(self): 
    print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Number of Doors: {self.num_doors}")

class Bike(Vehicle): 
  def __init__(self, brand, model, year, type): 
    super().__init__(brand, model, year) 
    self.type = type 

  def display_info(self): 
    print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Type: {self.type}")

car1 = Car("Toyota", "Camry", 2020, 4)
car1.display_info()
bike1 = Bike("Yamaha", "YZF-R3", 2021, "Sport")
bike1.display_info()

# Output 
# Brand: Toyota, Model: Camry, Year: 2020, Number of Doors: 4
# Brand: Yamaha, Model: YZF-R3, Year: 2021, Type: Sport