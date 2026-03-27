# 2. Yêu cầu 
# 1. Class Person: name, age 

class Person: 
  def __init__ (self, name, age): 
    self.name = name 
    self.age = age 

  def display_info(self): 
    print(f"Name: {self.name}, Age: {self.age}")

class Student(Person): 
  def __init__ (self, name, age, student_id): 
    super().__init__(name, age) 
    self.student_id = student_id 

  def display_info(self): 
    super().display_info() 
    print(f"Student ID: {self.student_id}")
  
  def study(self): 
    print(f"{self.name} is studying.")

Student1 = Student("Alice", 20, "S12345")
Student1.display_info()
Student1.study()

# Output 
# Name: Alice, Age: 20
# Student ID: S12345
# Alice is studying.
  